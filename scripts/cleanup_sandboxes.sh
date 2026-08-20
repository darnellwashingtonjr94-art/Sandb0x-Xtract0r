#!/bin/bash
# cleanup_sandboxes.sh - Kill hanging sandboxes and clean temp files

echo "[!] Terminating rogue sandboxes..."
pkill -f "qemu-system"
pkill -f "firecracker"
docker rm -f $(docker ps -a -q --filter "name=sandbox-") 2>/dev/null

echo "[!] Cleaning up temporary storage..."
rm -rf ../storage/tmp/*
echo "Cleanup complete."
