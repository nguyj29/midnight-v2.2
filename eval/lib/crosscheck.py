"""Cross-checks: CLAP embeddings, nearest labelled neighbours, zero-shot style tags, and small LOO models.

These are evidence to check judgments against, not the judgments themselves.
"""
from __future__ import annotations

import csv
import json
import logging
from pathlib import Path

import numpy as np

from . import audio_io, scale

log = logging.getLogger("crosscheck")
CLAP_ID = "laion/larger_clap_music_and_speech"  # larger_clap_music collapses under transformers 5 (see README)
WIN_S = 10.0
MAX_WINDOWS = 30

TAGS = {
    "style": ["ambient", "lo-fi hip hop beat", "jazz", "jazz fusion", "solo classical piano", "orchestral film score",
              "post-rock", "math rock", "progressive rock", "heavy metal", "synthwave", "house music", "techno",
              "drum and bass", "breakcore", "dubstep", "trip-hop", "downtempo chillout", "glitchy IDM electronica",
              "video game soundtrack", "chiptune", "funk", "neo-soul", "bossa nova", "latin music", "reggae",
              "acoustic folk", "new age", "minimalist music", "neoclassical", "trap beat", "future bass",
              "UK garage", "vaporwave", "shoegaze", "psychedelic rock", "blues", "gospel", "world music",
              "epic cinematic trailer music", "boom bap hip hop", "jungle", "anime soundtrack", "indie rock",
              "electronic dance music", "chamber music", "piano and strings"],
    "instrument": ["piano", "acoustic guitar", "distorted electric guitar", "clean electric guitar", "bass guitar",
                   "synth bass", "synthesizer pads", "lead synthesizer", "string section", "brass section",
                   "saxophone", "flute", "acoustic drum kit", "drum machine", "808 bass", "choir", "vocal chops",
                   "bells", "marimba", "harp", "organ", "electric piano", "arpeggiator", "orchestra", "violin",
                   "cello", "upright bass", "sampled breakbeat"],
    "mood": ["happy", "sad", "melancholic", "energetic", "calm", "dark", "tense", "dreamy", "nostalgic",
             "aggressive", "uplifting", "romantic", "mysterious", "playful", "epic", "peaceful", "anxious",
             "triumphant", "bittersweet", "hypnotic"],
    "production": ["lo-fi recording", "polished modern production", "live band recording", "heavily compressed",
                   "spacious reverb", "dry close-miked sound", "vintage analog sound", "distorted and noisy",
                   "minimal sparse arrangement", "dense layered arrangement", "home demo quality"],
}


# ------------------------------------------------------------------ embeddings
def clap_embeddings(eval_dir: Path, root: Path, tracks: list[tuple[str, str]]):
    out_dir = eval_dir / "crosscheck"
    out_dir.mkdir(exist_ok=True)
    f_emb = out_dir / "clap_embeddings.npz"
    ids = [t for t, _ in tracks]
    if f_emb.exists():
        z = np.load(f_emb, allow_pickle=True)
        if list(z["ids"]) == ids:
            return z["emb"], dict(np.load(out_dir / "clap_text.npz", allow_pickle=True))
    import torch
    from transformers import ClapModel, ClapProcessor
    model = ClapModel.from_pretrained(CLAP_ID).eval()
    proc = ClapProcessor.from_pretrained(CLAP_ID)
    sr = proc.feature_extractor.sampling_rate
    embs = []
    for tid, split in tracks:
        y = audio_io.decode(root / "blind" / split / f"{tid}.mp3", sr, mono=True)
        n = int(WIN_S * sr)
        starts = list(range(0, max(len(y) - n, 1), n))
        if len(starts) > MAX_WINDOWS:
            starts = [starts[i] for i in np.linspace(0, len(starts) - 1, MAX_WINDOWS).astype(int)]
        chunks = [y[s:s + n] for s in starts]
        chunks = [c for c in chunks if np.sqrt(np.mean(c ** 2)) > 1e-3] or chunks
        vecs = []
        with torch.inference_mode():
            for i in range(0, len(chunks), 8):
                inp = proc(audio=chunks[i:i + 8], sampling_rate=sr, return_tensors="pt")
                e = model.get_audio_features(**inp)
                e = getattr(e, "pooler_output", e)
                vecs.append(torch.nn.functional.normalize(e, dim=-1).numpy())
        v = np.concatenate(vecs).mean(0)
        embs.append(v / np.linalg.norm(v))
        log.info("  clap %s (%d windows)", tid, len(chunks))
    emb = np.stack(embs)
    text = {}
    with torch.inference_mode():
        for cat, words in TAGS.items():
            prompts = [f"This is a {w} music piece." if cat != "instrument" else f"Music featuring {w}." for w in words]
            inp = proc(text=prompts, return_tensors="pt", padding=True)
            t = model.get_text_features(**inp)
            t = getattr(t, "pooler_output", t)
            text[cat] = torch.nn.functional.normalize(t, dim=-1).numpy()
    np.savez(f_emb, ids=np.array(ids), emb=emb)
    np.savez(out_dir / "clap_text.npz", **text)
    return emb, text


def write_tags(eval_dir: Path, ids, emb, text):
    """Per-track zero-shot tags: raw top matches and what stands out relative to the collection."""
    for cat in TAGS:
        sims = emb @ text[cat].T  # (tracks, words)
        text[cat + "_sims"] = sims
    for i, tid in enumerate(ids):
        L = [f"# CLAP zero-shot tags — {tid}", "",
             f"Model `{CLAP_ID}`, track embedding = mean of {WIN_S:.0f}s windows. 'Top' = highest raw text-audio "
             "similarity; 'stands out' = highest z-score relative to the other tracks in this collection. "
             "Weak, style-level evidence only: CLAP often confuses neighbouring genres.", ""]
        for cat, words in TAGS.items():
            sims = text[cat + "_sims"]
            raw = sims[i]
            zc = (sims - sims.mean(0)) / (sims.std(0) + 1e-9)
            top = np.argsort(-raw)[:6]
            zs = np.argsort(-zc[i])[:5]
            L.append(f"- **{cat}** top: " + ", ".join(f"{words[j]} ({raw[j]:.2f})" for j in top))
            L.append(f"  - stands out: " + ", ".join(f"{words[j]} (z={zc[i, j]:+.1f})" for j in zs))
        (eval_dir / "packets" / tid / "clap_tags.md").write_text("\n".join(L) + "\n")


def write_neighbors(eval_dir: Path, tracks, emb):
    ids = [t for t, _ in tracks]
    split = dict(tracks)
    S = emb @ emb.T
    labeled = [i for i, t in enumerate(ids) if split[t] == "labeled"]
    rows = []
    for i, tid in enumerate(ids):
        cands = [j for j in labeled if j != i]
        order = sorted(cands, key=lambda j: -S[i, j])[:5]
        rows.append({"id": tid, "split": split[tid],
                     "neighbors": ";".join(f"{ids[j]}:{S[i, j]:.3f}" for j in order)})
    with open(eval_dir / "crosscheck" / "neighbors.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "split", "neighbors"])
        w.writeheader()
        w.writerows(rows)
    np.save(eval_dir / "crosscheck" / "similarity.npy", S)
    off = S[~np.eye(len(S), dtype=bool)]
    L = ["# Nearest labelled neighbours (CLAP cosine similarity)", "",
         f"Collection-wide off-diagonal similarity: median {np.median(off):.3f}, p10 {np.percentile(off, 10):.3f}, "
         f"p90 {np.percentile(off, 90):.3f}.", "", "| track | split | top-5 labelled neighbours |", "|---|---|---|"]
    for r in rows:
        L.append(f"| {r['id']} | {r['split']} | {r['neighbors'].replace(';', ', ')} |")
    (eval_dir / "crosscheck" / "neighbors.md").write_text("\n".join(L) + "\n")
    return S


# ------------------------------------------------------------------ small models
FEATURES = {
    # name: (description, extractor(features.json dict) -> float)
    "pulse_clarity": ("beat-tracker activation at beats (groove definiteness)", lambda m: m["pulse_clarity"]),
    "harmonic_richness": ("share of bars whose fitted chord is a 7th/9th/6th/sus/dim (not plain triad/power)",
                          lambda m: rich_share(m)),
    "dynamic_contrast_db": ("per-bar loudness p90 - p10 (arrangement dynamics)",
                            lambda m: m["global"]["loud_db_p10_p90"][1] - m["global"]["loud_db_p10_p90"][0]),
    "section_variety": ("distinct section letters", lambda m: len({s["letter"] for s in m["sections"]})),
    "melody_presence": ("share of bars with a skyline melody",
                        lambda m: m["melody"].get("bars_with_melody", 0) / max(m["n_bars"], 1)),
    "tempo_bpm": ("median tempo", lambda m: m["tempo_bpm_median"]),
    "integrated_lufs": ("mastering loudness (confound probe)", lambda m: m["quality"]["integrated_lufs"]),
}


def rich_share(m):
    q = dict((k, v) for k, v in m["harmony"].get("note_derived_chord_qualities", []))
    tot = sum(q.values())
    rich = sum(v for k, v in q.items() if k not in ("maj", "m", "5"))
    return rich / tot if tot else 0.0


def feature_table(eval_dir: Path, ids):
    X = []
    for tid in ids:
        m = json.loads((eval_dir / "packets" / tid / "features.json").read_text())
        X.append([float(f(m)) for _, (_, f) in FEATURES.items()])
    return np.array(X)


def loo_models(eval_dir: Path, root: Path, tracks, S):
    labels_path = root / "labels.csv"
    if not labels_path.exists():
        log.warning("labels.csv missing; skipping models")
        return
    from scipy.stats import spearmanr
    from sklearn.linear_model import RidgeCV
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    rows = scale.read_labels(labels_path)
    anchored = scale.anchored_scores(rows)
    ids = [t for t, _ in tracks]
    split = dict(tracks)
    lab_ids = [r["id"] for r in rows]
    X_all = feature_table(eval_dir, ids)
    idx = {t: i for i, t in enumerate(ids)}
    X = X_all[[idx[t] for t in lab_ids]]
    y = np.array([anchored[t] for t in lab_ids])
    alphas = np.logspace(-1, 3, 20)
    feat_names = list(FEATURES)

    def ridge():
        return make_pipeline(StandardScaler(), RidgeCV(alphas=alphas))

    results = {}
    for name, cols in {"ridge_all7": list(range(len(feat_names))),
                       "ridge_music6 (no LUFS)": [i for i, f in enumerate(feat_names) if f != "integrated_lufs"],
                       "lufs_only": [feat_names.index("integrated_lufs")]}.items():
        preds = []
        for k in range(len(lab_ids)):
            tr = [j for j in range(len(lab_ids)) if j != k]
            mdl = ridge().fit(X[tr][:, cols], y[tr])
            preds.append(float(mdl.predict(X[k:k + 1, cols])[0]))
        preds = np.array(preds)
        results[name] = summarize(y, preds, lab_ids, rows)
        results[name]["loo_pred"] = dict(zip(lab_ids, np.round(preds, 1).tolist()))
        full = ridge().fit(X[:, cols], y)
        coefs = full[-1].coef_
        results[name]["coef_std_units"] = {feat_names[c]: round(float(v), 2) for c, v in zip(cols, coefs)}
        results[name]["alpha"] = float(full[-1].alpha_)
        unl = [t for t in ids if split[t] == "unlabeled"]
        pu = full.predict(X_all[[idx[t] for t in unl]][:, cols])
        results[name]["unlabeled_pred"] = {t: round(float(p), 1) for t, p in zip(unl, pu)}
        results[name]["unlabeled_tier"] = {t: scale.tier_of(float(p)) for t, p in zip(unl, pu)}

    # similarity-weighted kNN on CLAP embeddings (k=3)
    lab_idx = [idx[t] for t in lab_ids]
    preds = []
    for k, t in enumerate(lab_ids):
        others = [j for j in range(len(lab_ids)) if j != k]
        sims = np.array([S[idx[t], lab_idx[j]] for j in others])
        top = np.argsort(-sims)[:3]
        w = np.maximum(sims[top], 1e-3)
        preds.append(float(np.sum(w * y[np.array(others)[top]]) / w.sum()))
    results["clap_knn3"] = summarize(y, np.array(preds), lab_ids, rows)
    results["clap_knn3"]["loo_pred"] = dict(zip(lab_ids, np.round(preds, 1).tolist()))
    unl = [t for t in ids if split[t] == "unlabeled"]
    ku = {}
    for t in unl:
        sims = np.array([S[idx[t], j] for j in lab_idx])
        top = np.argsort(-sims)[:3]
        w = np.maximum(sims[top], 1e-3)
        ku[t] = round(float(np.sum(w * y[top]) / w.sum()), 1)
    results["clap_knn3"]["unlabeled_pred"] = ku
    results["clap_knn3"]["unlabeled_tier"] = {t: scale.tier_of(p) for t, p in ku.items()}

    # feature correlations with the anchored score (for the taste profile's confound check)
    corr = {}
    for j, f in enumerate(feat_names):
        rho, p = spearmanr(X[:, j], y)
        corr[f] = {"spearman_rho": round(float(rho), 2), "p": round(float(p), 3)}
    results["feature_spearman_vs_score"] = corr
    results["features"] = {f: d for f, (d, _) in FEATURES.items()}
    results["feature_values"] = {t: dict(zip(feat_names, np.round(X_all[idx[t]], 3).tolist())) for t in ids}
    (eval_dir / "crosscheck" / "models.json").write_text(json.dumps(results, indent=1))
    L = ["# Leave-one-out cross-check models", "",
         "Target = anchored score (see labeled_scores.csv). Ridge with standardised features; alpha chosen by "
         "internal CV inside each training fold. Tier accuracy maps predicted score to a tier via band midpoints.", "",
         "| model | Spearman (LOO) | exact tier | within one tier | MAE (points) |", "|---|---|---|---|---|"]
    for name in ["ridge_all7", "ridge_music6 (no LUFS)", "lufs_only", "clap_knn3"]:
        r = results[name]
        L.append(f"| {name} | {r['spearman']:.2f} (p={r['spearman_p']:.2f}) | {r['exact_tier']:.0%} | "
                 f"{r['within_one_tier']:.0%} | {r['mae']:.1f} |")
    L += ["", "## Ridge coefficients (all labelled data, per 1 SD of feature)", ""]
    for name in ["ridge_all7", "ridge_music6 (no LUFS)"]:
        L.append(f"- {name} (alpha {results[name]['alpha']:.1f}): {results[name]['coef_std_units']}")
    L += ["", "## Single-feature Spearman correlation with anchored score (n=18)", ""]
    for f, v in corr.items():
        L.append(f"- {f}: rho {v['spearman_rho']:+.2f} (p={v['p']:.3f}) — {FEATURES[f][0]}")
    (eval_dir / "crosscheck" / "models.md").write_text("\n".join(L) + "\n")
    log.info("  models written")


def summarize(y, preds, lab_ids, rows):
    from scipy.stats import spearmanr
    tiers = {r["id"]: r["tier"] for r in rows}
    true_t = [tiers[t] for t in lab_ids]
    pred_t = [scale.tier_of(p) for p in preds]
    order = scale.TIER_ORDER
    exact = np.mean([a == b for a, b in zip(true_t, pred_t)])
    one = np.mean([abs(order.index(a) - order.index(b)) <= 1 for a, b in zip(true_t, pred_t)])
    rho, p = spearmanr(y, preds)
    return {"spearman": float(rho), "spearman_p": float(p), "exact_tier": float(exact), "within_one_tier": float(one),
            "mae": float(np.mean(np.abs(y - preds)))}


def run_all(eval_dir: Path, root: Path, tracks):
    emb, text = clap_embeddings(eval_dir, root, tracks)
    ids = [t for t, _ in tracks]
    write_tags(eval_dir, ids, emb, dict(text))
    S = write_neighbors(eval_dir, tracks, emb)
    # Blindness guard: the label-reading models only run once every track has blind listening notes.
    missing = [t for t in ids if not (eval_dir / "packets" / t / "listening_notes.md").exists()]
    if missing:
        log.warning("  skipping label-based models: %d tracks still lack listening_notes.md", len(missing))
        return
    loo_models(eval_dir, root, tracks, S)
