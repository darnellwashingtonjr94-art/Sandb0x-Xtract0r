FROM debian:bullseye-slim

# Suppress interactive prompts during package installation
ARG DEBIAN_FRONTEND=noninteractive

# Update and install dependencies with --fix-missing to handle mirror sync issues
RUN apt-get update && \
    apt-get install -y --no-install-recommends --fix-missing \
    build-essential \
    libmagickwand-dev \
    tshark \
    wkhtmltopdf \
    qemu-system-x86 \
    qemu-utils \
    adb \
    docker.io \
    git \
    curl && \
    rm -rf /var/lib/apt/lists/*
