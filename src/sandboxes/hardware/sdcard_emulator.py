import subprocess
from sandboxes.base import BaseSandbox

class SDCardEmulator(BaseSandbox):
    """Runner to emulate SD Card interfaces via Loopback devices."""
    
    def __init__(self, sandbox_id: str):
        super().__init__(sandbox_id, "SD-Card")
        self.img_path = f"/tmp/sdcard_{self.sandbox_id}.img"
        self.loop_dev = None

    def provision(self) -> bool:
        self.logger.info("Allocating block storage for SD Card emulation.")
        subprocess.run(["fallocate", "-l", "1G", self.img_path])
        return True

    def start(self) -> bool:
        self.logger.info("Attaching SD image to loop device...")
        result = subprocess.run(["losetup", "-f", "--show", self.img_path], capture_output=True, text=True)
        self.loop_dev = result.stdout.strip()
        self.is_running = True
        return True

    def detonate(self, payload_path: str) -> dict:
        self.logger.info(f"Simulating SD Card insertion and monitoring {self.loop_dev} IO...")
        return {"status": "detonated", "engine": "SD-Card"}

    def teardown(self) -> bool:
        if self.loop_dev:
            subprocess.run(["losetup", "-d", self.loop_dev])
        self.is_running = False
        return True
