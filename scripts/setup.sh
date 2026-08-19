#!/usr/bin/env bash
set -e

echo "=========================================="
echo " Setting up S@ndb0x-Xtract0r Environment  "
echo "=========================================="

# Create virtual environment if not present
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "[+] Created Python virtual environment."
fi

source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary runtime directories
mkdir -p storage/samples storage/artifacts storage/reports config/profiles

if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "[!] Created .env from template. Please add your API keys!"
fi

echo "[SUCCESS] Environment setup complete. Run ./scripts/detonate.sh to test."
