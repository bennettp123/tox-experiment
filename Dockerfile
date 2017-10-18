FROM library/alpine:3.5
RUN apk add --no-cache \
    python \
    python3 \
    py-pip \
    py-virtualenv \
 && pip install tox
 #   py-tox
 #&& virtualenv venv \
 #&& . venv/bin/activate \
 #&& pip install tox

