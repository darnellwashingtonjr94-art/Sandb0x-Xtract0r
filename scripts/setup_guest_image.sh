#!/bin/bash
# capture_pcap.sh - Wrapper for tcpdump on sandbox interfaces
# Usage: ./capture_pcap.sh <interface_name> <output_file.pcap>

IFACE=$1
OUTFILE=$2

if [ -z "$IFACE" ] || [ -z "$OUTFILE" ]; then
    echo "Usage: $0 <interface> <output_file.pcap>"
    exit 1
fi

echo "[+] Starting capture on $IFACE. Saving to $OUTFILE..."
# Requires sudo; typically run by the orchestrator
sudo tcpdump -i "$IFACE" -w "$OUTFILE" -U
