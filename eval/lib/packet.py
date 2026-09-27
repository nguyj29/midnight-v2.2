"""Build a listening packet for one track.

Stages (expensive ones are cached inside the packet so reruns are cheap):
  1. stems        Demucs htdemucs_6s -> stems/*.mp3
  2. beats        beat_this (+ madmom DBN post-processing) -> data/beats.json
  3. transcribe   Basic Pitch per pitched stem, band-onset drum transcription -> data/notes_*.json
  4. chords       madmom deep-chroma chord recogniser on the drumless mix -> data/chords_raw.json
  5. analysis     bars, sections, key, chords per bar, microtiming, quality, text views, images
"""
from __future__ import annotations

import json
import logging
import math
import tempfile
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

from . import audio_io

log = logging.getLogger("packet")

SR = 44100
STEMS = ["drums", "bass", "other", "vocals", "guitar", "piano"]
PITCHED = ["bass", "other", "vocals", "guitar", "piano"]
STEM_LETTER = {"drums": "D", "bass": "B", "other": "O", "vocals": "V", "guitar": "G", "piano": "P"}
NOTE_NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
PACKET_VERSION = 4


def pname(m: int) -> str:
    return f"{NOTE_NAMES[m % 12]}{m // 12 - 1}"


def db(x, floor=-120.0):
    return np.maximum(20 * np.log10(np.maximum(x, 1e-12)), floor)


def fmt_t(s: float) -> str:
    return f"{int(s // 60)}:{s % 60:04.1f}"


# --------------------------------------------------------------------------------------------
# Stage 1: source separation
# --------------------------------------------------------------------------------------------
_SEPARATOR = None


def stage_stems(mix: np.ndarray, pdir: Path) -> dict[str, np.ndarray]:
    sdir = pdir / "stems"
    if all((sdir / f"{s}.mp3").exists() for s in STEMS):
        return {s: audio_io.decode(sdir / f"{s}.mp3", SR) [: len(mix)] for s in STEMS}
    global _SEPARATOR
    import torch
    from demucs.api import Separator
    if _SEPARATOR is None:
        _SEPARATOR = Separator(model="htdemucs_6s", device="cpu", shifts=1, overlap=0.25, progress=False)
    t0 = time.time()
    _, out = _SEPARATOR.separate_tensor(torch.from_numpy(mix.T.copy()), SR)
    sdir.mkdir(parents=True, exist_ok=True)
    stems = {}
    for name, wav in out.items():
        arr = wav.numpy().T.astype(np.float32)
        audio_io.encode(arr, SR, sdir / f"{name}.mp3")
        stems[name] = arr
    log.info("  demucs %.0fs", time.time() - t0)
    return stems


# --------------------------------------------------------------------------------------------
# Stage 2: beats / downbeats
# --------------------------------------------------------------------------------------------
_BEAT_MODEL = None


def stage_beats(mono: np.ndarray, pdir: Path) -> dict:
    f = pdir / "data" / "beats.json"
    if f.exists():
        return json.loads(f.read_text())
    global _BEAT_MODEL
    import torch
    from beat_this.inference import Audio2Frames
    from beat_this.model.postprocessor import Postprocessor
    if _BEAT_MODEL is None:
        _BEAT_MODEL = Audio2Frames(checkpoint_path="final0", device="cpu")
    beat_logits, db_logits = _BEAT_MODEL(mono, SR)
    beat_p = torch.sigmoid(beat_logits).numpy()
    db_p = torch.sigmoid(db_logits).numpy()
    method = "beat_this final0 + madmom DBN"
    try:
        beats, downbeats = Postprocessor(type="dbn")(beat_logits, db_logits)
    except Exception as e:  # pragma: no cover - fallback path
        log.warning("  DBN postprocessing failed (%s); using minimal", e)
        beats, downbeats = Postprocessor(type="minimal")(beat_logits, db_logits)
        method = "beat_this final0 + minimal peak picking"
    beats = np.asarray(beats, dtype=float)
    downbeats = np.asarray(downbeats, dtype=float)
    fps = 50
    idx = np.clip((beats * fps).round().astype(int), 0, len(beat_p) - 1)
    clarity = float(np.mean(beat_p[idx])) if len(idx) else 0.0
    if len(beats) < 16:
        import librosa
        y22 = librosa.resample(mono, orig_sr=SR, target_sr=22050)
        _, bt = librosa.beat.beat_track(y=y22, sr=22050, units="time")
        if len(bt) >= 16:
            beats, method = np.asarray(bt), "librosa beat_track fallback (beat_this found <16 beats)"
            downbeats = beats[::4]
        else:
            dur = len(mono) / SR
            beats = np.arange(0, dur, 1.0)
            downbeats = beats[::4]
            method = "synthetic 60 BPM grid (no pulse detected)"
    res = {"beats": beats.tolist(), "downbeats": downbeats.tolist(), "method": method,
           "pulse_clarity": clarity,
           "beat_activation_mean": float(beat_p.mean()), "downbeat_activation_mean": float(db_p.mean())}
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(res))
    return res


def smooth_beats(b: np.ndarray, half: int = 4) -> np.ndarray:
    """Local linear fit over +-half beats; keeps a beat unchanged where the local tempo is not steady."""
    b = np.asarray(b, dtype=float)
    if len(b) < 2 * half + 1:
        return b
    out = b.copy()
    idx = np.arange(len(b))
    for i in range(len(b)):
        lo, hi = max(0, i - half), min(len(b), i + half + 1)
        x, y = idx[lo:hi], b[lo:hi]
        A = np.vstack([x, np.ones_like(x)]).T
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        fit = A @ coef
        ibi = coef[0]
        if ibi > 0 and np.std(y - fit) < 0.05 * ibi:
            out[i] = coef[0] * i + coef[1]
    return out


class Grid:
    """Beat/bar grid built from beat and downbeat times."""

    def __init__(self, beats, downbeats, duration):
        b = smooth_beats(np.asarray(beats, dtype=float))
        d = np.asarray(downbeats, dtype=float)
        ibi = float(np.median(np.diff(b))) if len(b) > 1 else 0.5
        # extend the beat list so that every time in [0, duration] is covered
        pre = []
        t = b[0] - ibi
        while t > -ibi:
            pre.append(t)
            t -= ibi
        post = []
        t = b[-1] + ibi
        while t < duration + ibi:
            post.append(t)
            t += ibi
        self.beats = np.concatenate([pre[::-1], b, post])
        self.n_real = (len(pre), len(pre) + len(b))
        # bar index per beat: a new bar starts at each downbeat (matched to nearest beat)
        is_db = np.zeros(len(self.beats), bool)
        for x in d:
            k = int(np.argmin(np.abs(self.beats - x)))
            if abs(self.beats[k] - x) < 0.35 * ibi:
                is_db[k] = True
        if not is_db.any():
            is_db[::4] = True
        # extrapolate the meter outside the tracked region using the typical bar length
        db_idx = np.flatnonzero(is_db)
        bpb = int(Counter(np.diff(db_idx)).most_common(1)[0][0]) if len(db_idx) > 1 else 4
        k = db_idx[0] - bpb
        while k >= 0:
            is_db[k] = True
            k -= bpb
        k = db_idx[-1] + bpb
        while k < len(self.beats):
            is_db[k] = True
            k += bpb
        self.beats_per_bar_mode = bpb
        # bars: bar 1 starts at first downbeat >= 0 s; beats before it form bar 0 (pickup)
        first = next(i for i in np.flatnonzero(is_db) if self.beats[i] >= -1e-6 or i == np.flatnonzero(is_db)[-1])
        bar_of = np.zeros(len(self.beats), int)
        pos_in = np.zeros(len(self.beats), int)
        bar = 0
        pos = 0
        for i in range(len(self.beats)):
            if i >= first and is_db[i]:
                bar += 1
                pos = 0
            bar_of[i] = bar
            pos_in[i] = pos
            pos += 1
        # beats before `first` belong to bar 0; renumber their positions to end at the bar length
        pre_idx = np.flatnonzero(np.arange(len(self.beats)) < first)
        if len(pre_idx):
            pos_in[pre_idx] = np.arange(len(pre_idx)) - len(pre_idx) + bpb
            pos_in[pre_idx] = np.maximum(pos_in[pre_idx], 0)
        self.bar_of, self.pos_in = bar_of, pos_in
        self.subdiv = 4
        self.duration = duration
        starts = {}
        for i in range(len(self.beats)):
            starts.setdefault(bar_of[i], i)
        self.bars = []  # list of dict(bar, start, end, beats)
        keys = sorted(starts)
        for j, bnum in enumerate(keys):
            i0 = starts[bnum]
            i1 = starts[keys[j + 1]] if j + 1 < len(keys) else len(self.beats) - 1
            t0, t1 = self.beats[i0], self.beats[i1]
            if t1 <= 0 or t0 >= duration:
                continue
            ib = np.diff(self.beats[i0:i1 + 1])
            self.bars.append({"bar": int(bnum), "start": float(max(t0, 0.0)), "end": float(min(t1, duration)),
                              "beats": int(i1 - i0), "beat_start_idx": int(i0),
                              "bpm": float(60 / np.median(ib)) if len(ib) else None})
        # drop a tiny bar 0 pickup (< 1 beat of audio)
        if self.bars and self.bars[0]["bar"] == 0 and self.bars[0]["end"] - self.bars[0]["start"] < 0.5 * ibi:
            self.bars = self.bars[1:]
        # drop a trailing fragment bar (the audio ends a fraction of a bar after the last downbeat): its
        # tempo and onset rate would be meaningless (e.g. "1363 BPM")
        if len(self.bars) > 2:
            typical = float(np.median([b["end"] - b["start"] for b in self.bars]))
            if self.bars[-1]["end"] - self.bars[-1]["start"] < 0.5 * typical:
                self.bars = self.bars[:-1]

    def locate(self, t: float):
        """Return (bar, beat_float 1-based, beat_index, frac) for a time in seconds."""
        k = int(np.searchsorted(self.beats, t, side="right") - 1)
        k = min(max(k, 0), len(self.beats) - 2)
        span = self.beats[k + 1] - self.beats[k]
        frac = (t - self.beats[k]) / span if span > 0 else 0.0
        return int(self.bar_of[k]), 1 + self.pos_in[k] + frac, k, frac

    def label(self, t: float) -> str:
        bar, beat, k, _ = self.locate(t)
        # a hit a few ms before the next downbeat belongs (for reading purposes) to beat 1 of the next bar
        if k + 1 < len(self.beats) and self.bar_of[k + 1] != bar and self.beats[k + 1] - t < 0.02:
            bar, beat = int(self.bar_of[k + 1]), 1.0
        return f"{bar:03d}:{beat:4.2f}"

    def beats_between(self, t0, t1):
        """Duration in beats between two times."""
        def cont(t):
            k = int(np.searchsorted(self.beats, t, side="right") - 1)
            k = min(max(k, 0), len(self.beats) - 2)
            span = self.beats[k + 1] - self.beats[k]
            return k + (t - self.beats[k]) / span
        return cont(t1) - cont(t0)


# --------------------------------------------------------------------------------------------
# Stage 3: transcription
# --------------------------------------------------------------------------------------------
_BP_MODEL = None
BP_RANGES = {"bass": (27.5, 400.0), "other": (None, None), "vocals": (60.0, None),
             "guitar": (70.0, None), "piano": (27.5, None)}


def stem_rms_db(x: np.ndarray, hop=1024, win=2048):
    import librosa
    m = x.mean(1) if x.ndim == 2 else x
    r = librosa.feature.rms(y=m, frame_length=win, hop_length=hop, center=True)[0]
    return db(r), hop / SR


def stage_transcribe(stems: dict, pdir: Path) -> dict:
    out = {}
    ddir = pdir / "data"
    ddir.mkdir(parents=True, exist_ok=True)
    for s in PITCHED:
        f = ddir / f"notes_{s}.json"
        if f.exists():
            out[s] = json.loads(f.read_text())
            continue
        out[s] = transcribe_pitched(stems[s], s)
        f.write_text(json.dumps(out[s]))
    f = ddir / "notes_drums.json"
    if f.exists():
        out["drums"] = json.loads(f.read_text())
    else:
        out["drums"] = transcribe_drums(stems["drums"])
        f.write_text(json.dumps(out["drums"]))
    return out


def transcribe_pitched(x: np.ndarray, name: str) -> dict:
    global _BP_MODEL
    from basic_pitch import ICASSP_2022_MODEL_PATH
    from basic_pitch.inference import Model, predict
    if _BP_MODEL is None:
        _BP_MODEL = Model(ICASSP_2022_MODEL_PATH)
    rms, hop_s = stem_rms_db(x)
    p95 = float(np.percentile(rms, 95))
    info = {"stem": name, "p95_rms_db": p95, "notes": [], "status": "ok"}
    if p95 < -50:
        info["status"] = "silent"
        return info
    mono = x.mean(1)
    lo, hi = BP_RANGES[name]
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / f"{name}.wav"
        audio_io.encode(mono, SR, wav, ["-ar", "22050", "-c:a", "pcm_s16le"])
        model_out, _, events = predict(wav, _BP_MODEL, onset_threshold=0.5, frame_threshold=0.3,
                                       minimum_note_length=80, minimum_frequency=lo, maximum_frequency=hi,
                                       melodia_trick=True)
    onset = model_out["onset"]  # (frames, 88); NOT linear in time (overlapping 2 s windows are unwrapped)
    from basic_pitch.note_creation import model_frames_to_time
    onset_times = model_frames_to_time(onset.shape[0])
    fps = 22050 / 256  # the librosa CQT below *is* linear in time
    import librosa
    y22 = librosa.resample(mono, orig_sr=SR, target_sr=22050)
    C = np.abs(librosa.cqt(y22, sr=22050, hop_length=256, fmin=27.5, n_bins=88, bins_per_octave=12))
    Cdb = db(C)
    cref = float(np.percentile(Cdb[Cdb > -100], 99.5)) if (Cdb > -100).any() else 0.0
    notes = []
    gate = max(-48.0, p95 - 35.0)  # drop bleed: notes where the stem is near-silent
    for (t0, t1, pitch, amp, _bends) in events:
        fi = int(round(t0 * fps))
        fo = int(np.searchsorted(onset_times, t0))
        pc = int(pitch) - 21
        opk = float(onset[max(fo - 2, 0): fo + 3, pc].max()) if 0 <= pc < onset.shape[1] else 0.0
        ri = int(t0 / hop_s)
        loc = float(np.max(rms[ri: ri + 3])) if ri < len(rms) else -120.0
        if loc < gate:
            continue
        # velocity: CQT level at the note's own pitch just after onset, relative to the stem's loudest notes
        e = float(Cdb[pc, fi: fi + 5].max()) if 0 <= pc < 88 and fi < Cdb.shape[1] else -120.0
        vel = int(np.clip(127 + (e - cref) * 2.5, 1, 127))
        conf = float(np.sqrt(max(amp, 0) * max(opk, 0.05)))  # frame posterior x onset posterior
        notes.append([round(float(t0), 3), round(float(t1), 3), int(pitch), vel, round(conf, 3), round(float(amp), 3)])
    notes.sort()
    info["notes"] = notes
    info["columns"] = ["start_s", "end_s", "midi", "velocity", "confidence", "frame_posterior"]
    return info


DRUM_BANDS = {"kick": (20, 150, 36), "snare": (150, 4000, 38), "hat": (5000, 16000, 42)}


def transcribe_drums(x: np.ndarray) -> dict:
    """Crude drum transcription: onset detection on three frequency bands of the drum stem."""
    import librosa
    mono = x.mean(1)
    rms, _ = stem_rms_db(x)
    p95 = float(np.percentile(rms, 95))
    info = {"stem": "drums", "p95_rms_db": p95, "hits": {}, "status": "ok"}
    if p95 < -50:
        info["status"] = "silent"
        return info
    y = librosa.resample(mono, orig_sr=SR, target_sr=32000)
    S = np.abs(librosa.stft(y, n_fft=1024, hop_length=320)) ** 2
    freqs = librosa.fft_frequencies(sr=32000, n_fft=1024)
    fps = 32000 / 320
    for band, (lo, hi, _) in DRUM_BANDS.items():
        m = (freqs >= lo) & (freqs < hi)
        env = librosa.onset.onset_strength(S=librosa.power_to_db(S[m]), sr=32000, hop_length=320, n_fft=1024)
        band_db = librosa.power_to_db(S[m].sum(0) + 1e-10)
        peaks = librosa.util.peak_pick(env, pre_max=3, post_max=3, pre_avg=10, post_avg=10,
                                       delta=0.25 * float(np.std(env)) + 1e-6, wait=5)
        if len(peaks) == 0:
            info["hits"][band] = []
            continue
        strengths = env[peaks]
        norm = float(np.percentile(strengths, 95)) or 1.0
        top = float(np.percentile(band_db, 99))
        hits = []
        for p, st in zip(peaks, strengths):
            if band_db[min(p + 1, len(band_db) - 1)] < top - 30:
                continue
            s = float(min(st / norm, 1.0))
            if s < 0.12:
                continue
            hits.append([round(float(p / fps), 3), round(s, 3)])
        info["hits"][band] = hits
    return info


# --------------------------------------------------------------------------------------------
# Stage 4: chords
# --------------------------------------------------------------------------------------------
def stage_chords(stems: dict, pdir: Path) -> dict:
    f = pdir / "data" / "chords_raw.json"
    if f.exists():
        return json.loads(f.read_text())
    from madmom.audio.chroma import DeepChromaProcessor
    from madmom.features.chords import DeepChromaChordRecognitionProcessor
    harm = sum(stems[s] for s in PITCHED).mean(1)
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / "harm.wav"
        audio_io.encode(harm, SR, wav, ["-c:a", "pcm_s16le"])
        chroma = DeepChromaProcessor()(str(wav))
        segs = DeepChromaChordRecognitionProcessor()(chroma)
    res = {"fps": 10, "chroma": np.round(chroma, 3).tolist(),
           "segments": [[float(a), float(b), str(l)] for a, b, l in segs]}
    f.write_text(json.dumps(res))
    return res


# --------------------------------------------------------------------------------------------
# Stage 5: analysis
# --------------------------------------------------------------------------------------------
KK_MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
KK_MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])

CHORD_TEMPLATES = {
    "": [0, 4, 7], "m": [0, 3, 7], "7": [0, 4, 7, 10], "maj7": [0, 4, 7, 11], "m7": [0, 3, 7, 10],
    "sus2": [0, 2, 7], "sus4": [0, 5, 7], "dim": [0, 3, 6], "m7b5": [0, 3, 6, 10], "aug": [0, 4, 8],
    "5": [0, 7], "6": [0, 4, 7, 9], "m6": [0, 3, 7, 9], "add9": [0, 2, 4, 7], "m9": [0, 2, 3, 7, 10],
    "maj9": [0, 2, 4, 7, 11],
}


def key_estimate(pc_hist: np.ndarray):
    scores = []
    for tonic in range(12):
        for mode, prof in (("major", KK_MAJ), ("minor", KK_MIN)):
            r = np.corrcoef(pc_hist, np.roll(prof, tonic))[0, 1]
            scores.append((float(r), f"{NOTE_NAMES[tonic]} {mode}"))
    scores.sort(reverse=True)
    return scores[:3]


def template_chord(pcs: np.ndarray, bass_pc: int | None):
    """Best-matching chord (root+quality) for a 12-d pitch-class weight vector."""
    if pcs.sum() <= 0:
        return None, 0.0
    v = pcs / (np.linalg.norm(pcs) + 1e-9)
    best = (None, -1.0)
    for root in range(12):
        for q, iv in CHORD_TEMPLATES.items():
            t = np.zeros(12)
            t[[(root + i) % 12 for i in iv]] = 1.0
            t[root] += 0.5  # root emphasis
            t /= np.linalg.norm(t)
            s = float(v @ t)
            if bass_pc is not None and bass_pc == root:
                s += 0.04
            s -= 0.012 * len(iv)  # mild preference for simpler chords
            if s > best[1]:
                best = (f"{NOTE_NAMES[root]}{q}", s)
    return best


def madmom_label(l: str) -> str:
    if l == "N":
        return "N"
    root, q = l.split(":")
    root = {"A#": "Bb", "D#": "Eb", "G#": "Ab", "Db": "C#", "Gb": "F#"}.get(root, root)
    return root + ("m" if q == "min" else "")


def bar_mean(frames: np.ndarray, fps: float, bars: list[dict]):
    out = []
    for b in bars:
        i0, i1 = int(b["start"] * fps), max(int(b["end"] * fps), int(b["start"] * fps) + 1)
        seg = frames[i0:i1]
        out.append(seg.mean(0) if len(seg) else np.zeros(frames.shape[1]))
    return np.array(out)


def segment_bars(F: np.ndarray, min_len: int = 4):
    """Checkerboard-kernel novelty on a bar-level self-similarity matrix -> boundary bar indices."""
    n = len(F)
    if n < 2 * min_len:
        return [0], np.zeros(n), np.eye(n)
    X = F - F.mean(0)
    X /= (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)
    S = X @ X.T
    L = 4
    g = np.exp(-0.5 * (np.linspace(-1.5, 1.5, 2 * L)) ** 2)
    K = np.outer(g, g) * np.kron(np.array([[1, -1], [-1, 1]]), np.ones((L, L)))
    P = np.pad(S, L, mode="edge")
    nov = np.array([np.sum(K * P[i:i + 2 * L, i:i + 2 * L]) for i in range(n)])
    nov = np.maximum(nov, 0)
    thr = nov.mean() + 0.5 * nov.std()
    cand = [i for i in range(1, n) if nov[i] >= thr and nov[i] == nov[max(0, i - 2): i + 3].max()]
    cand.sort(key=lambda i: -nov[i])
    chosen = []
    for i in cand:
        if i < min_len or n - i < min_len // 2:
            continue
        if all(abs(i - j) >= min_len for j in chosen):
            chosen.append(i)
    return [0] + sorted(chosen), nov, S


def label_sections(bounds, n, S):
    segs = [(bounds[i], bounds[i + 1] if i + 1 < len(bounds) else n) for i in range(len(bounds))]
    labels = []
    reps = []  # (label, segment)
    offdiag = S[~np.eye(n, dtype=bool)] if n > 1 else np.array([0.0])
    thr = float(np.percentile(offdiag, 70))
    for a, b in segs:
        best, bs = None, -9
        for lab, (c, d) in reps:
            sim = float(S[a:b, c:d].mean())
            if sim > bs:
                best, bs = lab, sim
        if best is not None and bs >= thr:
            labels.append(best)
        else:
            lab = chr(ord("A") + len(reps)) if len(reps) < 26 else f"Z{len(reps)}"
            reps.append((lab, (a, b)))
            labels.append(lab)
    return segs, labels


def build_analysis(tid: str, src: Path, pdir: Path, mix: np.ndarray, stems: dict, beats: dict,
                   notes: dict, chords_raw: dict):
    import librosa
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    mono = mix.mean(1)
    duration = len(mono) / SR
    grid = Grid(beats["beats"], beats["downbeats"], duration)
    bars = grid.bars
    nb = len(bars)
    real_beats = np.asarray(beats["beats"])
    # tempo from the smoothed grid: raw tracker beats are quantised to 20 ms (50 fps), so the median raw
    # interval snaps to e.g. 0.42 s (142.9 BPM) when the true beat is 0.4286 s (140 BPM)
    ibis = np.diff(smooth_beats(real_beats))
    bpm_med = 60.0 / float(np.median(ibis)) if len(ibis) else float("nan")

    # ---------------- frame features ----------------
    y22 = librosa.resample(mono, orig_sr=SR, target_sr=22050)
    hop = 512
    ffps = 22050 / hop
    rms = librosa.feature.rms(y=y22, hop_length=hop)[0]
    cent = librosa.feature.spectral_centroid(y=y22, sr=22050, hop_length=hop)[0]
    mfcc = librosa.feature.mfcc(y=y22, sr=22050, n_mfcc=13, hop_length=hop).T
    onsets = librosa.onset.onset_detect(y=y22, sr=22050, hop_length=hop, units="time")
    stem_rms = {s: stem_rms_db(stems[s], hop=1024)[0] for s in STEMS}
    sfps = SR / 1024

    chroma = np.asarray(chords_raw["chroma"])
    cfps = chords_raw["fps"]

    # ---------------- per-bar table ----------------
    bar_rows = []
    stem_bar_db = {s: [] for s in STEMS}
    for b in bars:
        i0, i1 = int(b["start"] * ffps), max(int(b["end"] * ffps), int(b["start"] * ffps) + 1)
        r = rms[i0:i1]
        c = cent[i0:i1]
        n_on = int(((onsets >= b["start"]) & (onsets < b["end"])).sum())
        dur = b["end"] - b["start"]
        row = {"bar": b["bar"], "start": round(b["start"], 2), "dur": round(dur, 2),
               "bpm": round(b["bpm"], 1) if b.get("bpm") else None,
               "loud_db": round(float(db(np.sqrt(np.mean(r ** 2)) if len(r) else 0)), 1),
               "bright_hz": int(np.median(c)) if len(c) else 0,
               "onsets_per_s": round(n_on / dur, 2) if dur > 0 else 0}
        j0, j1 = int(b["start"] * sfps), max(int(b["end"] * sfps), int(b["start"] * sfps) + 1)
        for s in STEMS:
            seg = stem_rms[s][j0:j1]
            stem_bar_db[s].append(float(db(np.sqrt(np.mean((10 ** (seg / 20)) ** 2)))) if len(seg) else -120.0)
        bar_rows.append(row)
    stem_bar_db = {s: np.array(v) for s, v in stem_bar_db.items()}
    loud_all = np.array([r["loud_db"] for r in bar_rows])
    max_loud = float(np.percentile(loud_all, 98)) if nb else 0
    for i, row in enumerate(bar_rows):
        row["rel_db"] = round(row["loud_db"] - max_loud, 1)
        mix_db = row["loud_db"]
        act = []
        for s in STEMS:
            v = stem_bar_db[s][i]
            if v > -48 and v > mix_db - 20:
                act.append(STEM_LETTER[s])
        row["active"] = "".join(act) or "-"
    stem_active = {s: np.array([STEM_LETTER[s] in r["active"] for r in bar_rows]) for s in STEMS}

    # ---------------- chords per bar ----------------
    segs = chords_raw["segments"]
    pitched_notes = []  # (t0,t1,midi,vel,conf,stem)
    for s in PITCHED:
        for n in notes[s]["notes"]:
            pitched_notes.append((n[0], n[1], n[2], n[3], n[4], s))
    pitched_notes.sort()
    pn_arr = np.array([(n[0], n[1], n[2], n[3], n[4]) for n in pitched_notes]) if pitched_notes else np.zeros((0, 5))
    pn_stem = [n[5] for n in pitched_notes]
    bar_chord, bar_chord2, bar_pcs, bar_notechord = [], [], [], []
    for b in bars:
        ov = defaultdict(float)
        for a, e, l in segs:
            o = min(e, b["end"]) - max(a, b["start"])
            if o > 0:
                ov[madmom_label(l)] += o
        dur = b["end"] - b["start"]
        ranked = sorted(ov.items(), key=lambda kv: -kv[1])
        lab = ranked[0][0] if ranked else "N"
        if len(ranked) > 1 and ranked[1][1] > 0.3 * dur:
            # order the two chords by time of appearance
            first = [madmom_label(l) for a, e, l in segs if e > b["start"] and a < b["end"]]
            ordered = [c for c in dict.fromkeys(first) if c in (ranked[0][0], ranked[1][0])]
            lab = " > ".join(ordered)
        bar_chord.append(lab)
        # pitch-class weights from transcribed notes sounding in the bar
        pcs = np.zeros(12)
        bass_w = np.zeros(12)
        if len(pn_arr):
            m = (pn_arr[:, 0] < b["end"]) & (pn_arr[:, 1] > b["start"])
            for k in np.flatnonzero(m):
                t0, t1, p, v, c = pn_arr[k]
                w = (min(t1, b["end"]) - max(t0, b["start"])) * (v / 127) * c
                pcs[int(p) % 12] += w
                if pn_stem[k] == "bass":
                    bass_w[int(p) % 12] += w
        bar_pcs.append(pcs)
        bpc = int(np.argmax(bass_w)) if bass_w.sum() > 0 else None
        lab2, sc = template_chord(pcs, bpc)
        if lab2 and bpc is not None and not lab2.startswith(NOTE_NAMES[bpc]) and bass_w.max() > 0.3 * bass_w.sum():
            lab2 = f"{lab2}/{NOTE_NAMES[bpc]}"
        bar_notechord.append(f"{lab2}" if lab2 and sc > 0.55 else "?")
        top = [NOTE_NAMES[i] for i in np.argsort(-pcs)[:5] if pcs[i] > 0.12 * pcs.max()] if pcs.max() > 0 else []
        bar_chord2.append(" ".join(top))
    for i, row in enumerate(bar_rows):
        row["chord"] = bar_chord[i]
        row["notes_chord"] = bar_notechord[i]
        row["pcs"] = bar_chord2[i]

    # key
    pc_total = np.sum(bar_pcs, axis=0) if nb else np.zeros(12)
    chroma_total = chroma.sum(0)
    key_notes = key_estimate(pc_total) if pc_total.sum() > 0 else []
    key_chroma = key_estimate(chroma_total)

    # ---------------- sections ----------------
    Fch = bar_mean(chroma, cfps, bars)
    Fmf = bar_mean(mfcc, ffps, bars)
    Fst = np.stack([np.clip(stem_bar_db[s], -60, 0) for s in STEMS], 1)
    Fen = loud_all[:, None]

    def z(A):
        return (A - A.mean(0)) / (A.std(0) + 1e-6)
    F = np.hstack([z(Fch) * 1.0, z(Fmf[:, 1:]) * 0.8, z(Fst) * 1.0, z(Fen) * 1.5]) if nb else np.zeros((0, 1))
    bounds, nov, SSM = segment_bars(F, 4)
    sec_segs, sec_labels = label_sections(bounds, nb, SSM) if nb else ([], [])
    q33, q66 = (np.percentile(loud_all, [33, 66]) if nb else (0, 0))
    sections = []
    counts = Counter()
    for (a, b_), lab in zip(sec_segs, sec_labels):
        counts[lab] += 1
        sub = bar_rows[a:b_]
        lm = float(np.mean([r["loud_db"] for r in sub]))
        rel = lm - max_loud  # dB below the track's loud bars (98th pct)
        lvl = "high" if rel > -4 else ("mid" if rel > -10 else "low")
        stems_on = [s for s in STEMS if stem_active[s][a:b_].mean() > 0.5]
        ch = [r["chord"] for r in sub]
        loop = chord_loop(ch)
        sections.append({"label": f"{lab}{counts[lab]}", "letter": lab, "bar_start": bars[a]["bar"],
                         "bar_end": bars[b_ - 1]["bar"], "n_bars": b_ - a,
                         "t_start": round(bars[a]["start"], 1), "t_end": round(bars[b_ - 1]["end"], 1),
                         "energy": lvl, "mean_db": round(lm, 1),
                         "bpm": round(float(np.median([r["bpm"] for r in sub if r["bpm"]] or [0])), 1),
                         "stems": [STEM_LETTER[s] for s in stems_on],
                         "chords": loop,
                         "bright_hz": int(np.median([r["bright_hz"] for r in sub])),
                         "onsets_per_s": round(float(np.mean([r["onsets_per_s"] for r in sub])), 2)})
    bar_section = {}
    for sec in sections:
        for bn in range(sec["bar_start"], sec["bar_end"] + 1):
            bar_section[bn] = sec["label"]
    for row in bar_rows:
        row["section"] = bar_section.get(row["bar"], "")

    # ---------------- microtiming ----------------
    micro = microtiming(grid, notes, stems)

    # ---------------- stem / transcription stats ----------------
    stem_stats = {}
    for s in PITCHED:
        ns = notes[s]["notes"]
        act = float(stem_active[s].mean()) if nb else 0.0
        if not ns:
            stem_stats[s] = {"status": notes[s]["status"], "active_bar_frac": round(act, 2), "n_notes": 0}
            continue
        arr = np.array(ns)
        poly = polyphony(arr)
        stem_stats[s] = {
            "status": notes[s]["status"], "active_bar_frac": round(act, 2), "n_notes": len(ns),
            "range": f"{pname(int(arr[:, 2].min()))}-{pname(int(arr[:, 2].max()))}",
            "median_pitch": pname(int(np.median(arr[:, 2]))),
            "mean_conf": round(float(arr[:, 4].mean()), 2),
            "low_conf_frac": round(float((arr[:, 4] < 0.35).mean()), 2),
            "vel_median": int(np.median(arr[:, 3])), "vel_std": round(float(arr[:, 3].std()), 1),
            "mean_polyphony": round(poly, 2),
            "median_dur_beats": round(float(np.median([grid.beats_between(a, b) for a, b in arr[:, :2]])), 2),
        }
    drum_stats = {"status": notes["drums"]["status"],
                  "active_bar_frac": round(float(stem_active["drums"].mean()), 2) if nb else 0,
                  "hits": {k: len(v) for k, v in notes["drums"].get("hits", {}).items()}}

    melody = melody_analysis(grid, notes, bars)
    harmony = harmony_analysis(bar_chord, bar_notechord, sections)

    # ---------------- quality / mastering ----------------
    quality = audio_io.probe(src)
    quality.update(audio_io.ebur128(src))
    peak = float(np.abs(mix).max())
    quality["sample_peak_dbfs"] = round(float(db(peak)), 2)
    quality["crest_db"] = round(float(db(peak) - db(np.sqrt(np.mean(mono ** 2)))), 1)
    quality["clipped_sample_frac"] = float((np.abs(mix) > 0.995).mean())
    spec = np.abs(librosa.stft(mono[: SR * 120] if len(mono) > SR * 120 else mono, n_fft=4096, hop_length=4096)) ** 2
    ps = spec.mean(1)
    fr = librosa.fft_frequencies(sr=SR, n_fft=4096)
    psdb = 10 * np.log10(ps + 1e-20)
    ref = np.percentile(psdb[(fr > 200) & (fr < 4000)], 50)
    above = fr[psdb > ref - 50]
    quality["bandwidth_hz"] = int(above.max()) if len(above) else 0
    mid = mix.mean(1)
    side = (mix[:, 0] - mix[:, 1]) / 2
    quality["stereo_side_to_mid_db"] = round(float(db(np.sqrt(np.mean(side ** 2))) - db(np.sqrt(np.mean(mid ** 2)))), 1)
    quality["noise_floor_db"] = round(float(np.percentile(db(rms), 5)), 1)

    # ---------------- write outputs ----------------
    meta = {
        "id": tid, "packet_version": PACKET_VERSION, "duration_s": round(duration, 1),
        "tempo_bpm_median": round(bpm_med, 1),
        "tempo_cv_pct": round(float(np.std(ibis) / np.mean(ibis) * 100), 2) if len(ibis) else None,
        "beats_per_bar_mode": grid.beats_per_bar_mode, "n_bars": nb,
        "beat_method": beats["method"], "pulse_clarity": round(beats["pulse_clarity"], 3),
        "key_from_notes": key_notes, "key_from_chroma": key_chroma,
        "sections": sections, "stems": stem_stats, "drums": drum_stats,
        "microtiming": micro, "melody": melody, "harmony": harmony, "quality": quality,
        "global": {
            "loud_db_mean": round(float(loud_all.mean()), 1) if nb else None,
            "loud_db_p10_p90": [round(float(np.percentile(loud_all, 10)), 1), round(float(np.percentile(loud_all, 90)), 1)] if nb else None,
            "bright_hz_median": int(np.median(cent)),
            "onsets_per_s": round(len(onsets) / duration, 2),
            "stem_share_db": {s: round(float(np.percentile(stem_rms[s], 90)), 1) for s in STEMS},
        },
    }
    (pdir / "features.json").write_text(json.dumps(meta, indent=1))
    write_beats_csv(pdir, grid, real_beats)
    write_bars(pdir, bar_rows)
    write_notes_text(pdir, grid, notes)
    write_midi(pdir, notes, bpm_med)
    write_chords(pdir, bar_rows, segs, grid)
    write_sections(pdir, meta)
    write_score(pdir, grid, bars, bar_rows, notes, sections)
    write_summary(pdir, meta, bar_rows)
    plot_images(pdir, y22, chroma, cfps, bars, bar_rows, sections, stem_bar_db, duration, plt, librosa)
    return meta


def chord_loop(ch: list[str]) -> str:
    """Compact description of a chord sequence: run-length merge, then detect a repeating cycle."""
    if not ch:
        return ""
    rl = []
    for c in ch:
        if rl and rl[-1][0] == c:
            rl[-1][1] += 1
        else:
            rl.append([c, 1])
    seq = [c for c, _ in rl]
    for L in range(1, min(8, len(seq)) + 1):
        cyc = seq[:L]
        match = sum(1 for i, c in enumerate(seq) if c == cyc[i % L])
        if len(seq) >= 2 * L and match / len(seq) >= 0.8:
            return "loop[" + " ".join(f"{c}" for c in cyc) + f"] x{len(seq) / L:.1f}"
    s = " ".join(f"{c}({n})" if n > 1 else c for c, n in rl[:16])
    return s + (" ..." if len(rl) > 16 else "")


def polyphony(arr: np.ndarray) -> float:
    if len(arr) == 0:
        return 0.0
    ev = sorted([(a, 1) for a in arr[:, 0]] + [(b, -1) for b in arr[:, 1]])
    cur, last, acc, tot = 0, ev[0][0], 0.0, 0.0
    for t, d in ev:
        if cur > 0:
            acc += cur * (t - last)
            tot += (t - last)
        cur += d
        last = t
    return acc / tot if tot > 0 else 0.0


def microtiming(grid: Grid, notes: dict, stems: dict) -> dict:
    res = {}
    lo, hi = grid.n_real
    b = grid.beats
    t_lo, t_hi = b[lo], b[hi - 1] if hi - 1 > lo else b[-1]

    dh = notes["drums"].get("hits", {})
    # subdivision: are off-beat onsets nearer a 16th grid or a triplet grid?
    allon = [h[0] for band in dh.values() for h in band if h[1] >= 0.3] + \
        [n[0] for s in PITCHED for n in notes[s]["notes"] if n[4] >= 0.4]
    d16 = tri = 0
    for t in allon:
        if not (t_lo <= t <= t_hi):
            continue
        _, _, _, frac = grid.locate(t)
        a = min(abs(frac - q) for q in (0, .25, .5, .75, 1))
        b3 = min(abs(frac - q) for q in (0, 1 / 3, 2 / 3, 1))
        if min(frac, 1 - frac) < 0.08:
            continue  # on the beat: uninformative
        if abs(a - b3) > 0.04:
            if a < b3:
                d16 += 1
            else:
                tri += 1
    if d16 + tri >= 20:
        res["subdivision"] = {"offbeat_onsets_nearer_16th": d16, "nearer_triplet": tri,
                              "triplet_share": round(tri / (d16 + tri), 2)}
    N = 6 if res.get("subdivision", {}).get("triplet_share", 0) > 0.55 else 4
    res["grid_steps_per_beat"] = N
    grid.subdiv = N
    def devs(times):
        out = []
        for t in times:
            if not (t_lo <= t <= t_hi):
                continue
            _, _, k, frac = grid.locate(t)
            q = round(frac * N) / N
            span = b[k + 1] - b[k]
            out.append(((frac - q) * span * 1000, (frac - q) * N, frac))
        return np.array(out) if out else np.zeros((0, 3))

    groups = {}
    groups["drums"] = [h[0] for band in dh.values() for h in band if h[1] >= 0.3]
    for s in PITCHED:
        groups[s] = [n[0] for n in notes[s]["notes"]]
    for g, times in groups.items():
        d = devs(times)
        if len(d) < 20:
            continue
        res[g] = {"n": int(len(d)), "mean_ms": round(float(d[:, 0].mean()), 1),
                  "mean_abs_ms": round(float(np.abs(d[:, 0]).mean()), 1),
                  "sd_ms": round(float(d[:, 0].std()), 1),
                  "within_10ms_frac": round(float((np.abs(d[:, 0]) < 10).mean()), 2),
                  "on_16th_grid_frac": round(float((np.abs(d[:, 1]) < 0.15).mean()), 2)}
    # swing: position of off-beat eighth onsets inside the beat (0.5 = straight, 0.667 = triplet swing)
    sw = []
    src = [h[0] for h in dh.get("hat", [])] + [h[0] for h in dh.get("snare", [])]
    if len(src) < 30:
        src = groups["drums"] + [n[0] for s in PITCHED for n in notes[s]["notes"]]
    for t in src:
        if not (t_lo <= t <= t_hi):
            continue
        _, _, _, frac = grid.locate(t)
        if 0.42 <= frac <= 0.72:
            sw.append(frac)
    if len(sw) >= 15:
        pos = float(np.median(sw))
        res["swing"] = {"offbeat_position": round(pos, 3), "swing_ratio": round(pos / (1 - pos), 2), "n": len(sw)}
    # 16th swing
    sw16 = []
    for t in src:
        if not (t_lo <= t <= t_hi):
            continue
        _, _, _, frac = grid.locate(t)
        f2 = (frac * 2) % 1.0
        if 0.42 <= f2 <= 0.72:
            sw16.append(f2)
    if len(sw16) >= 15:
        pos = float(np.median(sw16))
        res["swing16"] = {"offbeat_position": round(pos, 3), "swing_ratio": round(pos / (1 - pos), 2)}
    # accent profile by beat position (drum onset strength)
    acc = defaultdict(list)
    for band, hits in dh.items():
        for t, s in hits:
            if not (t_lo <= t <= t_hi):
                continue
            _, beat, _, frac = grid.locate(t)
            if frac < 0.15 or frac > 0.85:
                bi = int(round(beat)) if frac < 0.15 else int(beat) + 1
                if bi > grid.beats_per_bar_mode:
                    bi = 1
                acc[(band, bi)].append(s)
    prof = {}
    for band in dh:
        row = {}
        for bi in range(1, grid.beats_per_bar_mode + 1):
            v = acc.get((band, bi), [])
            row[str(bi)] = [len(v), round(float(np.mean(v)), 2) if v else 0]
        prof[band] = row
    res["drum_hits_by_beat[count,mean_strength]"] = prof
    # drum velocity variance
    allv = [h[1] for band in dh.values() for h in band]
    if allv:
        res["drum_strength_sd"] = round(float(np.std(allv)), 3)
    # tempo stability
    rb = grid.beats[lo:hi]
    if len(rb) > 8:
        ib = np.diff(rb)
        bpm = 60 / ib
        tt = rb[1:]
        slope = np.polyfit(tt, bpm, 1)[0] * 60 if len(tt) > 2 else 0
        res["tempo"] = {"ibi_cv_pct": round(float(ib.std() / ib.mean() * 100), 2),
                        "bpm_drift_per_min": round(float(slope), 2),
                        "local_bpm_p5_p95": [round(float(np.percentile(bpm, 5)), 1), round(float(np.percentile(bpm, 95)), 1)]}
    return res


def melody_analysis(grid: Grid, notes: dict, bars: list) -> dict:
    """Skyline melody from the non-bass pitched stems + motif repetition statistics."""
    evs = []
    for s in ["vocals", "other", "guitar", "piano"]:
        for n in notes[s]["notes"]:
            if n[4] >= 0.3:
                evs.append((n[0], n[2], s))
    if len(evs) < 10:
        return {"status": "too few notes"}
    evs.sort()
    # skyline: highest pitch per 16th slot
    sky = {}
    for t, p, s in evs:
        bar, beat, k, frac = grid.locate(t)
        slot = (k, int(round(frac * 4)))
        if slot not in sky or p > sky[slot][1]:
            sky[slot] = (t, p, s, bar)
    line = [sky[k] for k in sorted(sky)]
    pitches = np.array([x[1] for x in line])
    iv = np.diff(pitches)
    iv = iv[np.abs(iv) <= 24]
    step = float(np.mean(np.abs(iv) <= 2)) if len(iv) else 0
    leap = float(np.mean(np.abs(iv) >= 5)) if len(iv) else 0
    src = Counter(x[2] for x in line)
    # motifs: 4-note interval patterns (3 intervals)
    grams = defaultdict(list)
    for i in range(len(line) - 3):
        seq = tuple(int(line[j + 1][1] - line[j][1]) for j in range(i, i + 3))
        if max(abs(v) for v in seq) > 12 or all(v == 0 for v in seq):
            continue
        grams[seq].append(line[i][3])
    top = sorted(grams.items(), key=lambda kv: -len(kv[1]))[:6]
    motifs = []
    for seq, where in top:
        if len(where) < 3:
            continue
        bars_u = sorted(set(where))
        motifs.append({"intervals": list(seq), "count": len(where),
                       "bars": bars_u[:12] + (["..."] if len(bars_u) > 12 else [])})
    # coverage: fraction of bars where the skyline is active
    bars_with = len(set(x[3] for x in line))
    return {"skyline_notes": len(line), "range": f"{pname(int(pitches.min()))}-{pname(int(pitches.max()))}",
            "p10_p90": f"{pname(int(np.percentile(pitches, 10)))}-{pname(int(np.percentile(pitches, 90)))}",
            "stepwise_frac": round(step, 2), "leap_frac(>=4th)": round(leap, 2),
            "mean_abs_interval": round(float(np.mean(np.abs(iv))), 2) if len(iv) else 0,
            "skyline_source_stems": dict(src.most_common()), "bars_with_melody": bars_with,
            "bars_total": len(bars), "top_motifs": motifs}


def harmony_analysis(bar_chord, bar_notechord, sections) -> dict:
    n = len(bar_chord)
    if n == 0:
        return {}
    changes = sum(1 for i in range(1, n) if bar_chord[i] != bar_chord[i - 1]) + sum(" > " in c for c in bar_chord)
    uniq = Counter(c for bc in bar_chord for c in bc.split(" > "))
    rep4 = np.mean([bar_chord[i] == bar_chord[i - 4] for i in range(4, n)]) if n > 4 else 0
    rep8 = np.mean([bar_chord[i] == bar_chord[i - 8] for i in range(8, n)]) if n > 8 else 0
    # 4-bar progressions
    progs = Counter(tuple(bar_chord[i:i + 4]) for i in range(0, n - 3, 2))
    qual = Counter(c for c in bar_notechord if c != "?")
    richness = Counter()
    for c in bar_notechord:
        if c == "?":
            continue
        base = c.split("/")[0]
        root = base[:2] if len(base) > 1 and base[1] in "#b" else base[:1]
        richness[base[len(root):] or "maj"] += 1
    return {"chord_changes_per_bar": round(changes / n, 2), "distinct_chords": len(uniq),
            "most_common_chords": uniq.most_common(8),
            "same_chord_4_bars_later": round(float(rep4), 2), "same_chord_8_bars_later": round(float(rep8), 2),
            "top_4bar_progressions": [[" | ".join(p), c] for p, c in progs.most_common(4)],
            "note_derived_chord_qualities": richness.most_common(10),
            "note_derived_unknown_frac": round(bar_notechord.count("?") / n, 2)}


# ---------------------------------------------------------------- writers
def write_beats_csv(pdir, grid, real_beats):
    lines = ["time_s,bar,beat_in_bar,tracked"]
    lo, hi = grid.n_real
    for i, t in enumerate(grid.beats):
        if t < 0 or t > grid.duration:
            continue
        lines.append(f"{t:.3f},{grid.bar_of[i]},{grid.pos_in[i] + 1},{int(lo <= i < hi)}")
    (pdir / "beats.csv").write_text("\n".join(lines) + "\n")


def write_bars(pdir, rows):
    cols = ["bar", "start", "dur", "bpm", "loud_db", "rel_db", "bright_hz", "onsets_per_s", "active", "chord",
            "notes_chord", "pcs", "section"]
    lines = [",".join(cols)]
    for r in rows:
        lines.append(",".join(str(r.get(c, "")).replace(",", ";") for c in cols))
    (pdir / "bars.csv").write_text("\n".join(lines) + "\n")
    md = ["# Per-bar table", "",
          "loud_db = mix RMS dBFS; rel = dB below the track's loud bars; bright = median spectral centroid (Hz); "
          "ons/s = onsets per second; active stems: D drums, B bass, O other, V vocals/lead, G guitar, P piano; "
          "chord = madmom (maj/min only); notes = chord fitted to transcribed notes (richer but noisier).", "",
          "| bar | time | bpm | loud | rel | bright | ons/s | active | chord | notes | pcs | sec |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['bar']} | {fmt_t(r['start'])} | {r['bpm']} | {r['loud_db']} | {r['rel_db']} | {r['bright_hz']} | "
                  f"{r['onsets_per_s']} | {r['active']} | {r['chord']} | {r['notes_chord']} | {r['pcs']} | {r['section']} |")
    (pdir / "bars.md").write_text("\n".join(md) + "\n")


def write_notes_text(pdir, grid, notes):
    nd = pdir / "notes"
    nd.mkdir(exist_ok=True)
    for s in PITCHED:
        lines = [f"# {s} stem — Basic Pitch transcription ({notes[s]['status']})",
                 "# note  onset(bar:beat)  dur(beats)  velocity  confidence", ]
        for t0, t1, p, v, c, _ in notes[s]["notes"]:
            lines.append(f"{pname(p):4s}  {grid.label(t0)}  {grid.beats_between(t0, t1):5.2f}  {v:3d}  {c:.2f}")
        (nd / f"{s}.txt").write_text("\n".join(lines) + "\n")
    lines = ["# drums stem — band-onset transcription (kick <150 Hz, snare 150-4k, hat >5k)",
             "# instrument  onset(bar:beat)  strength(0-1, used as velocity/confidence)"]
    allh = sorted((t, band, s) for band, hits in notes["drums"].get("hits", {}).items() for t, s in hits)
    for t, band, s in allh:
        lines.append(f"{band:5s}  {grid.label(t)}  {s:.2f}")
    (nd / "drums.txt").write_text("\n".join(lines) + "\n")


def write_midi(pdir, notes, bpm):
    import pretty_midi
    md = pdir / "midi"
    md.mkdir(exist_ok=True)
    progs = {"bass": 33, "other": 81, "vocals": 65, "guitar": 26, "piano": 0}
    full = pretty_midi.PrettyMIDI(initial_tempo=bpm if bpm and not math.isnan(bpm) else 120)
    for s in PITCHED:
        pm = pretty_midi.PrettyMIDI(initial_tempo=bpm if bpm and not math.isnan(bpm) else 120)
        inst = pretty_midi.Instrument(program=progs[s], name=s)
        for t0, t1, p, v, c, _ in notes[s]["notes"]:
            inst.notes.append(pretty_midi.Note(velocity=int(v), pitch=int(p), start=float(t0), end=float(max(t1, t0 + 0.03))))
        pm.instruments.append(inst)
        pm.write(str(md / f"{s}.mid"))
        full.instruments.append(inst)
    dr = pretty_midi.Instrument(program=0, is_drum=True, name="drums")
    for band, hits in notes["drums"].get("hits", {}).items():
        for t, s in hits:
            dr.notes.append(pretty_midi.Note(velocity=int(20 + 107 * s), pitch=DRUM_BANDS[band][2], start=t, end=t + 0.05))
    pm = pretty_midi.PrettyMIDI(initial_tempo=bpm if bpm and not math.isnan(bpm) else 120)
    pm.instruments.append(dr)
    pm.write(str(md / "drums.mid"))
    full.instruments.append(dr)
    full.write(str(md / "all.mid"))


def write_chords(pdir, rows, segs, grid):
    lines = ["# Chord timeline", "",
             "Per bar. `madmom` = deep-chroma chord recogniser (major/minor/N only, reliable roots). "
             "`from notes` = best chord template fitted to the transcribed pitch classes (captures 7ths/sus/9ths "
             "but inherits transcription errors; '?' = no good fit). `pcs` = strongest pitch classes in the bar.", "",
             "| bar | time | madmom | from notes | pcs | section |", "|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['bar']} | {fmt_t(r['start'])} | {r['chord']} | {r['notes_chord']} | {r['pcs']} | {r['section']} |")
    lines += ["", "## Raw madmom segments (seconds)", ""]
    for a, e, l in segs:
        lines.append(f"- {fmt_t(a)}–{fmt_t(e)}  ({grid.label(a)})  {l}")
    (pdir / "chords.md").write_text("\n".join(lines) + "\n")


def write_sections(pdir, meta):
    lines = ["# Section map", "",
             f"Tempo ≈ {meta['tempo_bpm_median']} BPM (beat interval CV {meta['tempo_cv_pct']}%), "
             f"{meta['beats_per_bar_mode']} beats/bar, {meta['n_bars']} bars, beat source: {meta['beat_method']}, "
             f"pulse clarity {meta['pulse_clarity']} (0-1).", "",
             "Sections come from novelty on a bar-level self-similarity matrix (chroma + timbre + stem activity + "
             "loudness). Letters mark sections that resemble each other; they are not verse/chorus labels.", "",
             "| section | bars | time | energy | mean dB | bpm | stems | bright Hz | ons/s | chords |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for s in meta["sections"]:
        lines.append(f"| {s['label']} | {s['bar_start']}–{s['bar_end']} ({s['n_bars']}) | {fmt_t(s['t_start'])}–{fmt_t(s['t_end'])} | "
                     f"{s['energy']} | {s['mean_db']} | {s['bpm']} | {''.join(s['stems'])} | {s['bright_hz']} | "
                     f"{s['onsets_per_s']} | {s['chords']} |")
    (pdir / "sections.md").write_text("\n".join(lines) + "\n")


def drum_grid(grid, bar, hits_by_band):
    nbeats = bar["beats"] or grid.beats_per_bar_mode
    N = grid.subdiv
    steps = N * nbeats
    out = {}
    for band, hits in hits_by_band.items():
        row = ["."] * steps
        for t, s in hits:
            if not (bar["start"] - 0.03 <= t < bar["end"] - 0.03):
                continue
            bn, beat, _, _ = grid.locate(t)
            idx = int(round((beat - 1) * N)) if bn == bar["bar"] else int(round(grid.beats_between(bar["start"], t) * N))
            if 0 <= idx < steps:
                row[idx] = "X" if s >= 0.6 else ("x" if s >= 0.3 else "o")
        s = "".join(row)
        out[band] = " ".join(s[i:i + N] for i in range(0, steps, N))
    return out


def write_score(pdir, grid, bars, rows, notes, sections):
    """Compact per-bar multi-stem view."""
    by_stem = {s: np.array(notes[s]["notes"]) if notes[s]["notes"] else np.zeros((0, 6)) for s in PITCHED}
    hits = notes["drums"].get("hits", {})
    sec_start = {s["bar_start"]: s for s in sections}
    lines = ["# Score view", "",
             f"One block per bar. Drums: {grid.subdiv} steps per beat ({'16th-triplet' if grid.subdiv == 6 else '16th-note'} grid), one group per beat (X strong, x medium, o soft hit; K kick, S snare, "
             "H hat/cymbal). Pitched stems: note@beat (1-based within the bar), `~n` = held n beats, [..] = notes "
             "struck together, `?` suffix = low-confidence note (<0.35). Chord = madmom / fitted-from-notes.", ""]
    for b, r in zip(bars, rows):
        if b["bar"] in sec_start:
            s = sec_start[b["bar"]]
            lines += ["", f"## {s['label']}  bars {s['bar_start']}–{s['bar_end']}  ({fmt_t(s['t_start'])}–{fmt_t(s['t_end'])}, "
                      f"energy {s['energy']}, stems {''.join(s['stems'])})", ""]
        lines.append(f"**bar {b['bar']}**  {fmt_t(b['start'])}  {r['chord']} / {r['notes_chord']}  "
                     f"({r['loud_db']} dB, active {r['active']})")
        if STEM_LETTER["drums"] in r["active"] and hits:
            g = drum_grid(grid, b, hits)
            lines.append("    drums  " + "  ".join(f"{k[0].upper()}: {v}" for k, v in g.items()))
        for s in PITCHED:
            arr = by_stem[s]
            if not len(arr):
                continue
            m = (arr[:, 0] >= b["start"] - 0.02) & (arr[:, 0] < b["end"] - 0.02)
            sel = arr[m]
            if not len(sel):
                continue
            groups = []
            for n in sel:
                beat = grid.locate(n[0])[1] if grid.locate(n[0])[0] == b["bar"] else 1 + grid.beats_between(b["start"], n[0])
                if groups and abs(groups[-1][0] - beat) < 0.13:
                    groups[-1][1].append(n)
                else:
                    groups.append([beat, [n]])
            toks = []
            for beat, ns in groups[:18]:
                names = []
                seen = set()
                for n in sorted(ns, key=lambda n: n[2]):
                    if int(n[2]) in seen:
                        continue
                    seen.add(int(n[2]))
                    names.append(pname(int(n[2])) + ("?" if n[4] < 0.35 else ""))
                d = grid.beats_between(ns[0][0], ns[0][1])
                snap = 1 + round((beat - 1) * grid.subdiv) / grid.subdiv
                pos = snap if abs(snap - beat) < 0.08 else beat
                if pos >= (b["beats"] or grid.beats_per_bar_mode) + 1:
                    pos = beat  # an early note just before the next downbeat: show e.g. 3.95, never a beat 4 in 3/4
                tok = (names[0] if len(names) == 1 else "[" + " ".join(names) + "]") + f"@{pos:.2f}".rstrip("0").rstrip(".")
                if d >= 0.9:
                    tok += f"~{d:.1f}"
                toks.append(tok)
            if len(groups) > 18:
                toks.append(f"(+{len(groups) - 18} more)")
            lines.append(f"    {s:6s} " + " ".join(toks))
    (pdir / "score.md").write_text("\n".join(lines) + "\n")


def write_summary(pdir, meta, rows):
    q = meta["quality"]
    L = [f"# Packet summary — {meta['id']}", "",
         f"- Duration {fmt_t(meta['duration_s'])}; {meta['n_bars']} bars of {meta['beats_per_bar_mode']} beats; "
         f"tempo ≈ {meta['tempo_bpm_median']} BPM (beat-interval CV {meta['tempo_cv_pct']}%); "
         f"pulse clarity {meta['pulse_clarity']} ({meta['beat_method']}).",
         f"- Key estimate (from notes): " + ", ".join(f"{k} r={r:.2f}" for r, k in meta["key_from_notes"][:2]) +
         f"; (from chroma): " + ", ".join(f"{k} r={r:.2f}" for r, k in meta["key_from_chroma"][:2]),
         f"- Loudness: {q['integrated_lufs']} LUFS integrated, LRA {q['loudness_range_lu']} LU, true peak "
         f"{q['true_peak_dbtp']} dBTP, crest {q['crest_db']} dB; per-bar RMS p10/p90 {meta['global']['loud_db_p10_p90']} dBFS.",
         f"- Source file: {q['codec']} {q['bit_rate_kbps']} kbps {q['sample_rate']} Hz; bandwidth ≈ {q['bandwidth_hz']} Hz; "
         f"clipped samples {q['clipped_sample_frac']:.2e}; side/mid {q['stereo_side_to_mid_db']} dB; "
         f"quietest-5% frame level {q['noise_floor_db']} dB.",
         f"- Brightness median {meta['global']['bright_hz_median']} Hz; onset rate {meta['global']['onsets_per_s']}/s.",
         "", "## Stems", "",
         "| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for s, st in meta["stems"].items():
        if st["n_notes"] == 0:
            L.append(f"| {s} | {st['active_bar_frac']:.0%} | 0 ({st['status']}) | | | | | | | |")
            continue
        L.append(f"| {s} | {st['active_bar_frac']:.0%} | {st['n_notes']} | {st['range']} | {st['median_pitch']} | "
                 f"{st['mean_conf']} | {st['low_conf_frac']:.0%} | {st['vel_median']}/{st['vel_std']} | "
                 f"{st['mean_polyphony']} | {st['median_dur_beats']} |")
    d = meta["drums"]
    L.append(f"| drums | {d['active_bar_frac']:.0%} | hits {d['hits']} | | | | | | | |")
    L.append("")
    L.append("Stem level (90th pct RMS dBFS): " + ", ".join(f"{k} {v}" for k, v in meta["global"]["stem_share_db"].items()))
    L += ["", "## Sections", "", "| section | bars | time | energy | dB | stems | chords |", "|---|---|---|---|---|---|---|"]
    for s in meta["sections"]:
        L.append(f"| {s['label']} | {s['bar_start']}–{s['bar_end']} | {fmt_t(s['t_start'])}–{fmt_t(s['t_end'])} | "
                 f"{s['energy']} | {s['mean_db']} | {''.join(s['stems'])} | {s['chords']} |")
    h = meta["harmony"]
    L += ["", "## Harmony", "",
          f"- Chord changes per bar {h.get('chord_changes_per_bar')}; distinct chords {h.get('distinct_chords')}; "
          f"same chord 4 bars later {h.get('same_chord_4_bars_later')}, 8 bars later {h.get('same_chord_8_bars_later')}.",
          f"- Most common (madmom): {h.get('most_common_chords')}",
          f"- Common 4-bar progressions: {h.get('top_4bar_progressions')}",
          f"- Chord qualities fitted from notes: {h.get('note_derived_chord_qualities')} (unknown {h.get('note_derived_unknown_frac')})"]
    m = meta["melody"]
    L += ["", "## Melody (skyline of non-bass stems)", ""]
    if m.get("status"):
        L.append(f"- {m['status']}")
    else:
        L += [f"- {m['skyline_notes']} skyline notes, range {m['range']} (p10–p90 {m['p10_p90']}), "
              f"stepwise {m['stepwise_frac']:.0%}, leaps ≥4th {m['leap_frac(>=4th)']:.0%}, mean |interval| {m['mean_abs_interval']} st.",
              f"- Skyline comes from: {m['skyline_source_stems']}; melody present in {m['bars_with_melody']}/{m['bars_total']} bars.",
              "- Recurring 4-note interval motifs: " + "; ".join(f"{x['intervals']} ×{x['count']} (bars {x['bars']})" for x in m["top_motifs"])]
    mt = meta["microtiming"]
    L += ["", "## Microtiming & groove", "",
          f"Deviations are measured against a locally smoothed beat grid divided into {mt.get('grid_steps_per_beat', 4)} steps per beat "
          f"({'16th-note triplets' if mt.get('grid_steps_per_beat') == 6 else '16th notes'})."]
    for g in ["drums"] + PITCHED:
        if g in mt:
            v = mt[g]
            L.append(f"- {g}: n={v['n']}, mean offset {v['mean_ms']} ms, mean |dev| {v['mean_abs_ms']} ms, sd {v['sd_ms']} ms, "
                     f"{v['within_10ms_frac']:.0%} within 10 ms of the grid, {v['on_16th_grid_frac']:.0%} within 15% of a grid step")
    if "subdivision" in mt:
        L.append(f"- Subdivision: {mt['subdivision']['triplet_share']:.0%} of informative off-beat onsets sit nearer a triplet "
                 f"grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)")
    if "swing" in mt:
        L.append(f"- 8th swing: off-beat at {mt['swing']['offbeat_position']} of the beat (ratio {mt['swing']['swing_ratio']}; 1.0 straight, 2.0 triplet)")
    if "swing16" in mt:
        L.append(f"- 16th swing: ratio {mt['swing16']['swing_ratio']}")
    if "tempo" in mt:
        L.append(f"- Tempo: IBI CV {mt['tempo']['ibi_cv_pct']}%, drift {mt['tempo']['bpm_drift_per_min']} BPM/min, "
                 f"local BPM p5–p95 {mt['tempo']['local_bpm_p5_p95']}")
    if "drum_strength_sd" in mt:
        L.append(f"- Drum hit strength sd {mt['drum_strength_sd']}; hits by beat [count, mean strength]: "
                 f"{mt['drum_hits_by_beat[count,mean_strength]']}")
    L += ["", "## Files", "",
          "- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, "
          "`midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`"]
    (pdir / "summary.md").write_text("\n".join(L) + "\n")


def plot_images(pdir, y22, chroma, cfps, bars, rows, sections, stem_bar_db, duration, plt, librosa):
    import librosa.display  # noqa
    bounds_t = [s["t_start"] for s in sections[1:]]
    # mel spectrogram
    M = librosa.power_to_db(librosa.feature.melspectrogram(y=y22, sr=22050, hop_length=512, n_mels=128), ref=np.max)
    fig, ax = plt.subplots(figsize=(16, 5))
    librosa.display.specshow(M, sr=22050, hop_length=512, x_axis="time", y_axis="mel", ax=ax, cmap="magma")
    for t in bounds_t:
        ax.axvline(t, color="cyan", lw=1.2, ls="--")
    for s in sections:
        ax.text(s["t_start"] + 0.5, 11000, s["label"], color="cyan", fontsize=10, va="top")
    ax.set_title(f"Mel spectrogram ({pdir.name}); dashed = section boundaries")
    fig.tight_layout()
    fig.savefig(pdir / "mel.png", dpi=80)
    plt.close(fig)
    # chromagram (bar-synchronous, deep chroma)
    C = bar_mean(chroma, cfps, bars).T if bars else chroma.T
    fig, ax = plt.subplots(figsize=(16, 4))
    ax.imshow(C, aspect="auto", origin="lower", cmap="Greys", interpolation="nearest",
              extent=[bars[0]["bar"] - 0.5, bars[-1]["bar"] + 0.5, -0.5, 11.5])
    ax.set_yticks(range(12))
    ax.set_yticklabels(NOTE_NAMES)
    for s in sections[1:]:
        ax.axvline(s["bar_start"] - 0.5, color="red", lw=1.2, ls="--")
    for s in sections:
        ax.text(s["bar_start"], 11.4, s["label"], color="red", fontsize=9, va="top")
    ax.set_xlabel("bar")
    ax.set_title("Chromagram per bar (deep chroma of drumless mix); dashed = section boundaries")
    fig.tight_layout()
    fig.savefig(pdir / "chroma.png", dpi=80)
    plt.close(fig)
    # energy curve with stems
    x = [r["start"] for r in rows]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(16, 6), sharex=True, gridspec_kw={"height_ratios": [1, 1.2]})
    a1.plot(x, [r["loud_db"] for r in rows], color="k", lw=1.5, label="mix RMS dB")
    a1b = a1.twinx()
    a1b.plot(x, [r["bright_hz"] for r in rows], color="tab:orange", lw=1, alpha=0.7, label="brightness Hz")
    a1b.set_ylabel("centroid Hz", color="tab:orange")
    a1.set_ylabel("dBFS")
    cols = {"drums": "tab:gray", "bass": "tab:blue", "other": "tab:green", "vocals": "tab:red",
            "guitar": "tab:brown", "piano": "tab:purple"}
    for s in STEMS:
        a2.plot(x, np.clip(stem_bar_db[s], -60, 0), label=s, color=cols[s], lw=1.2)
    a2.set_ylabel("stem RMS dBFS")
    a2.legend(loc="lower right", ncol=6, fontsize=8)
    for ax in (a1, a2):
        for t in bounds_t:
            ax.axvline(t, color="red", lw=1, ls="--")
    for s in sections:
        a1.text(s["t_start"] + 0.5, a1.get_ylim()[1], s["label"], color="red", fontsize=9, va="top")
    a2.set_xlabel("seconds")
    a1.set_title("Energy curve (per bar) with section boundaries; lower panel = stem levels")
    fig.tight_layout()
    fig.savefig(pdir / "energy.png", dpi=80)
    plt.close(fig)


# --------------------------------------------------------------------------------------------
def build_packet(tid: str, src: Path, pdir: Path) -> dict:
    pdir.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    mix = audio_io.decode(src, SR)
    stems = stage_stems(mix, pdir)
    beats = stage_beats(mix.mean(1), pdir)
    notes = stage_transcribe(stems, pdir)
    chords = stage_chords(stems, pdir)
    meta = build_analysis(tid, src, pdir, mix, stems, beats, notes, chords)
    (pdir / "data" / "DONE").write_text(str(PACKET_VERSION))
    log.info("  packet %s done in %.0fs", tid, time.time() - t0)
    return meta
