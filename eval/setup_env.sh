#!/usr/bin/env bash
# Recreate eval/.venv (Python 3.12, CPU-only) entirely inside eval/. Nothing is installed outside the project folder.
set -euo pipefail
cd "$(dirname "$0")"
export PIP_CACHE_DIR="$PWD/.cache/pip" UV_CACHE_DIR="$PWD/.cache/uv" UV_PYTHON_INSTALL_DIR="$PWD/.uv/python"

python3 -m venv .bootstrap
.bootstrap/bin/pip install -q uv
UV="$PWD/.bootstrap/bin/uv"
"$UV" python install 3.12
"$UV" venv --python 3.12 .venv
export VIRTUAL_ENV="$PWD/.venv"

# CPU wheels of torch/torchaudio (torchaudio is only needed by beat_this's import chain)
"$UV" pip install --index-url https://download.pytorch.org/whl/cpu --extra-index-url https://pypi.org/simple \
    --index-strategy unsafe-best-match "torch==2.11.*" "torchaudio==2.11.*"
"$UV" pip install "demucs==4.1.0" "beat-this==1.1.0" "librosa>=0.11,<1" soundfile onnxruntime pretty-midi mir-eval \
    "resampy<0.4.3" scikit-learn scipy matplotlib pandas "transformers==5.17.0" soxr cython setuptools wheel
# basic-pitch 0.4.0 pins tensorflow<2.15.1 (no py3.12 / numpy 2 support); we run its bundled ONNX model instead
"$UV" pip install --no-deps "basic-pitch==0.4.0"
# madmom's PyPI release (2018) is broken on modern numpy; the git main branch is fixed
"$UV" pip install --no-build-isolation "madmom @ git+https://github.com/CPJKU/madmom.git@27f032e8947204902c675e5e341a3faf5dc86dae"
echo "done: run  python eval/run.py"
