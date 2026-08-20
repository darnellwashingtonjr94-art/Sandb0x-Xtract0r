#!/bin/bash
# cli_submit.sh - Submit a payload to the API for analysis
# Usage: ./cli_submit.sh <file_path> <os_target>

FILE_PATH=$1
TARGET_OS=${2:-"windows"}
API_URL="http://localhost:8000/api/submit"

if [ ! -f "$FILE_PATH" ]; then
    echo "File not found!"
    exit 1
fi

echo "[+] Submitting $FILE_PATH to $TARGET_OS sandbox..."
curl -X POST "$API_URL" \
  -F "file=@$FILE_PATH" \
  -F "os=$TARGET_OS"
