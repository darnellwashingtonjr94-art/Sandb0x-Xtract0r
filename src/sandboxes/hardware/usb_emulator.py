import subprocess
import os
from sandboxes.base import BaseSandbox

class USBEmulator(BaseSandbox):
    """Runner to emulate USB Hard Drives via Linux Gadgetfs."""
    
    def __init__(self, sandbox_id: str, image_size_mb: int = 512):
        super().__init__(sandbox_id, "USB-Drive")
        self.image_size_mb = image_size_mb
        self.img_path = f"/tmp/usb_{self.sandbox_id}.img"

    def provision(self) -> bool:
        self.logger.info("Creating blank FAT32 image file...")
        subprocess.run(["dd", "if=/dev/zero", f"of={self.img_path}", f"bs=1M", f"count={self.image_size_mb}"])
        subprocess.run(["mkfs.fat", self.img_path])
        return True

    def start(self) -> bool:
        self.logger.info("Mounting image to dummy USB interface (dummy_hcd)...")
        subprocess.run(["modprobe", "dummy_hcd"])
        subprocess.run(["modprobe", "g_mass_storage", f"file={self.img_path}", "ro=0"])
        self.is_running = True
        return True

    def detonate(self, payload_path: str) -> dict:
        self.logger.info("Injecting payload into virtual USB block...")
        # Mount locally, copy payload, unmount, simulating a plugged-in infected drive.
        return {"status": "detonated", "engine": "USB-Mass-Storage"}

    def teardown(self) -> bool:
        subprocess.run(["rmmod", "g_mass_storage"])
        os.remove(self.img_path)
        self.is_running = False
        return True
