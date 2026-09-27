"""Audio decode/encode helpers built on the ffmpeg CLI (no torchaudio I/O needed)."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import numpy as np


def decode(path: Path | str, sr: int = 44100, mono: bool = False) -> np.ndarray:
    """Decode any ffmpeg-readable file to float32. Returns (n,) if mono else (n, 2)."""
    ch = 1 if mono else 2
    cmd = ["ffmpeg", "-v", "error", "-nostdin", "-i", str(path), "-f", "f32le",
           "-acodec", "pcm_f32le", "-ac", str(ch), "-ar", str(sr), "-"]
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.float32).copy()
    return x if mono else x.reshape(-1, 2)


def encode(x: np.ndarray, sr: int, path: Path | str, codec_args: list[str] | None = None) -> None:
    """Encode float32 audio (n,) or (n, ch) to a file; format inferred from the extension."""
    x = np.asarray(x, dtype=np.float32)
    ch = 1 if x.ndim == 1 else x.shape[1]
    codec_args = codec_args or []
    if str(path).endswith(".mp3") and not codec_args:
        codec_args = ["-codec:a", "libmp3lame", "-b:a", "160k"]
    cmd = ["ffmpeg", "-v", "error", "-nostdin", "-y", "-f", "f32le", "-ac", str(ch), "-ar", str(sr),
           "-i", "-", *codec_args, str(path)]
    subprocess.run(cmd, check=True, input=np.ascontiguousarray(x).tobytes())


def probe(path: Path | str) -> dict:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
                         check=True, capture_output=True, text=True).stdout
    d = json.loads(out)
    st = next((s for s in d.get("streams", []) if s.get("codec_type") == "audio"), {})
    return {
        "codec": st.get("codec_name"),
        "sample_rate": int(st.get("sample_rate", 0) or 0),
        "channels": int(st.get("channels", 0) or 0),
        "bit_rate_kbps": round(int(st.get("bit_rate") or d.get("format", {}).get("bit_rate") or 0) / 1000),
        "duration_s": float(d.get("format", {}).get("duration") or 0),
    }


def ebur128(path: Path | str) -> dict:
    """Integrated loudness (LUFS), loudness range (LU) and true peak (dBTP) via ffmpeg's ebur128 filter."""
    res = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", str(path), "-af", "ebur128=peak=true",
                          "-f", "null", "-"], capture_output=True, text=True)
    txt = res.stderr
    summ = txt[txt.rfind("Summary:"):]

    def grab(pattern):
        m = re.search(pattern, summ)
        return float(m.group(1)) if m else None
    return {
        "integrated_lufs": grab(r"I:\s+(-?[\d.]+) LUFS"),
        "loudness_range_lu": grab(r"LRA:\s+(-?[\d.]+) LU"),
        "true_peak_dbtp": grab(r"Peak:\s+(-?[\d.]+) dBFS"),
    }
