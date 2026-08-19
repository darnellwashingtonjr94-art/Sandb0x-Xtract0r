#!/usr/bin/env bash
set -e

SAMPLE_FILE=${1:-"storage/samples/sample.exe"}

if [ ! -f "$SAMPLE_FILE" ]; then
    echo "[!] Sample file $SAMPLE_FILE not found."
    echo "Usage: ./scripts/detonate.sh <path_to_sample>"
    exit 1
fi

echo "[*] Detonating sample through S@ndb0x-Xtract0r pipeline..."
source venv/bin/activate
python src/main.py --file "$SAMPLE_FILE" --platform auto
