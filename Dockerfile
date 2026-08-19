FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install system dependencies for analysis tools and PDF generation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmagic1 \
    tshark \
    wkhtmltopdf \
    qemu-utils \
    android-tools-adb \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p storage/samples storage/artifacts storage/reports

ENTRYPOINT ["python", "src/main.py"]
CMD ["--help"]
