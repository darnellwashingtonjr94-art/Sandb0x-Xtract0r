FROM debian:bookworm-slim

# Link the container to your GitHub repository for GHCR tracking
LABEL org.opencontainers.image.source=https://github.com/credkellar-boop/SandB0x-Xtract0r

# Suppress interactive prompts during package installation
ARG DEBIAN_FRONTEND=noninteractive

# Update and install dependencies cleanly in a single layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
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
