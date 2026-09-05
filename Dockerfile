FROM debian:bullseye-slim

# Suppress interactive prompts during package installation
ARG DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
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

# Add the rest of your application code and instructions below
# COPY . /app
# WORKDIR /app
# CMD ["your-start-command"]
