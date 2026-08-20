#!/bin/bash
# healthcheck.sh - Verify host environment

echo "[+] Checking KVM virtualization..."
if [ -c "/dev/kvm" ]; then
    echo "  -> /dev/kvm exists. Hardware acceleration OK."
else
    echo "  -> WARNING: /dev/kvm not found. VMs will be slow."
fi

echo "[+] Checking API status..."
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/health || echo "Failed")
echo "  -> API returned: $HTTP_STATUS"
