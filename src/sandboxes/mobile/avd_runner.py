import subprocess
import time
from sandboxes.base import BaseSandbox

class AVDRunner(BaseSandbox):
    """Runner for Google Android Virtual Device (AVD)."""
    
    def __init__(self, sandbox_id: str, avd_name: str = "Pixel_6_API_33"):
        super().__init__(sandbox_id, "Android")
        self.avd_name = avd_name
        self.process = None

    def provision(self) -> bool:
        self.logger.info(f"Checking AVD {self.avd_name} availability...")
        return True

    def start(self) -> bool:
        self.process = subprocess.Popen(["emulator", "-avd", self.avd_name, "-no-snapshot-save"])
        time.sleep(15) # Wait for boot
        self.is_running = True
        return True

    def detonate(self, payload_path: str) -> dict:
        self.logger.info(f"Installing {payload_path} via adb...")
        subprocess.run(["adb", "install", payload_path])
        subprocess.run(["adb", "shell", "monkey", "-p", "com.malicious.app", "1"])
        return {"status": "detonated", "engine": "AVD"}

    def teardown(self) -> bool:
        subprocess.run(["adb", "emu", "kill"])
        self.is_running = False
        return True
