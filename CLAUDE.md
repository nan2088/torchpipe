## install and test
uv pip uninstall omniback torchpipe
export SETUPTOOLS_SCM_PRETEND_VERSION=0.1.24
uv pip install -e .
pytest tests

cd plugins/torchpipe/
uv pip install -e .
pytest tests
 