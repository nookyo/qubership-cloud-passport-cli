FROM ghcr.io/netcracker/base-images-module-base:main

USER root

COPY cp_image/build/requirements.txt /build/requirements.txt
COPY cp_image/build/pip.conf /etc/pip.conf
COPY cp_image/scripts /module/scripts

RUN test -d /module/venv || python3 -m venv /module/venv && \
    source /module/venv/bin/activate && \
    pip install --no-cache-dir -r /build/requirements.txt
