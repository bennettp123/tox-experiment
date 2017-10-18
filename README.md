# tox experiment

Tox is a wrapper for virtualenv that allows you to test
your project with multiple versions of python.

# Quickstart

Install both python2 and python3, then

```
tox
```

The sample module will be tested on both python2 and python3.

# Docker

If your environment doesn't include python 2 or 3, the included Dockerfile
builds a lightweight image with both python 2.7 and python 3.5.

Usage:

```
docker build -t alpine-python2-python3 .
docker run --rm -v `pwd`:/pwd -w /pwd  -it alpine-python2-python3 tox
```

