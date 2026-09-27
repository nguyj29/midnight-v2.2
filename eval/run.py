#!/usr/bin/env python3
"""Build every track's listening packet and the cross-checks.

    python eval/run.py                 # packets (cached stages reused) + cross-checks
    python eval/run.py --only t0d513ac8
    python eval/run.py --skip-packets  # cross-checks only
    python eval/run.py --force         # recompute expensive stages too

Works from the system Python: it re-executes itself inside eval/.venv (see setup_env.sh).
All caches and model weights live in eval/.cache, so nothing outside the project folder is touched.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

EVAL = Path(__file__).resolve().parent
ROOT = EVAL.parent
VENV_PY = EVAL / ".venv" / "bin" / "python"

if Path(sys.prefix).resolve() != (EVAL / ".venv").resolve():
    if not VENV_PY.exists():
        sys.exit(f"Missing {VENV_PY}. Create it first with: bash {EVAL / 'setup_env.sh'}")
    os.execv(str(VENV_PY), [str(VENV_PY), str(Path(__file__).resolve()), *sys.argv[1:]])

CACHE = EVAL / ".cache"
os.environ.setdefault("HF_HOME", str(CACHE / "huggingface"))
os.environ.setdefault("TORCH_HOME", str(CACHE / "torch"))
os.environ.setdefault("MPLCONFIGDIR", str(CACHE / "matplotlib"))
os.environ.setdefault("NUMBA_CACHE_DIR", str(CACHE / "numba"))
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE))
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ["TMPDIR"] = str(CACHE / "tmp")  # keep temporary WAVs inside the project folder
(CACHE / "tmp").mkdir(parents=True, exist_ok=True)

import argparse  # noqa: E402
import logging  # noqa: E402
import shutil  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402
import warnings  # noqa: E402

warnings.filterwarnings("ignore")
(EVAL / "logs").mkdir(exist_ok=True)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S",
                    handlers=[logging.StreamHandler(), logging.FileHandler(EVAL / "logs" / "run.log")])
for noisy in ("root", "numba", "matplotlib", "httpx", "huggingface_hub"):
    logging.getLogger(noisy).setLevel(logging.ERROR)
sys.path.insert(0, str(EVAL))
log = logging.getLogger("run")


def list_tracks():
    tracks = []
    for split in ("labeled", "unlabeled"):
        for p in sorted((ROOT / "blind" / split).glob("*.mp3")):
            tracks.append((p.stem, split, p))
    return tracks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="track ids to process")
    ap.add_argument("--force", action="store_true", help="recompute cached expensive stages")
    ap.add_argument("--skip-packets", action="store_true")
    ap.add_argument("--skip-crosschecks", action="store_true")
    args = ap.parse_args()

    tracks = list_tracks()
    if args.only:
        tracks = [t for t in tracks if t[0] in set(args.only)]
    log.info("%d tracks", len(tracks))
    failures = []
    if not args.skip_packets:
        from lib.packet import build_packet
        for i, (tid, split, path) in enumerate(tracks, 1):
            pdir = EVAL / "packets" / tid
            if args.force and pdir.exists():
                for sub in ("stems", "data"):
                    shutil.rmtree(pdir / sub, ignore_errors=True)
            log.info("[%d/%d] %s (%s)", i, len(tracks), tid, split)
            try:
                build_packet(tid, path, pdir)
            except Exception:
                failures.append(tid)
                log.error("packet failed for %s\n%s", tid, traceback.format_exc())
    if not args.skip_crosschecks and not args.only:
        from lib import crosscheck
        t0 = time.time()
        crosscheck.run_all(EVAL, ROOT, [(t, s) for t, s, _ in list_tracks()])
        log.info("cross-checks done in %.0fs", time.time() - t0)
    if failures:
        log.error("FAILED: %s", failures)
        sys.exit(1)
    log.info("all done")


if __name__ == "__main__":
    main()
