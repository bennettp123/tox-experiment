# Tox experiment

Tox is a wrapper for virtualenv that allows you to test
your project with multiple versions of python.

# Quickstart

Install both python2 and python3, then

```
pip install tox
tox
```

The sample module will be tested on both python2 and python3.

To run the tests, you'll also need `pip install pytest`.

The included tox.ini uses any installed version of python 2 and python 3.
If you want to be more specific, change `py2` to `py27`, `py3`  to `py35`,
etc.

# Docker

If your environment doesn't include python 2 or 3, the included Dockerfile
builds a lightweight image with both python 2.7 and python 3.5.

Usage:

```
docker build -t alpine-python2-python3 .
docker run --rm -v `pwd`:/pwd -w /pwd  -it alpine-python2-python3 tox
```

