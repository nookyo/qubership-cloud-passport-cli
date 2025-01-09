FROM ghcr.io/netcracker/base-images-module-base:main

USER root

COPY build/requirements.txt /build/requirements.txt
COPY build/pip.conf /etc/pip.conf
COPY scripts /module/scripts

RUN test -d /module/venv || python3 -m venv /module/venv && \
    source /module/venv/bin/activate && \
    pip install --no-cache-dir -r /build/requirements.txt
