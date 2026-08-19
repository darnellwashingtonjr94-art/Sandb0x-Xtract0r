import subprocess
from sandboxes.base import BaseSandbox

class QemuRunner(BaseSandbox):
    """Runner for QEMU-based virtualization (Legacy Windows/Linux)."""
    
    def __init__(self, sandbox_id: str, image_path: str, memory: int = 2048):
        super().__init__(sandbox_id, "QEMU")
        self.image_path = image_path
        self.memory = memory
        self.process = None

    def provision(self) -> bool:
        self.logger.info(f"Provisioning QEMU image at {self.image_path}")
        return True

    def start(self) -> bool:
        cmd = [
            "qemu-system-x86_64",
            "-m", str(self.memory),
            "-hda", self.image_path,
            "-net", "nic", "-net", "user",
            "-snapshot" # Ensures changes are discarded
        ]
        self.process = subprocess.Popen(cmd)
        self.is_running = True
        return True

    def detonate(self, payload_path: str) -> dict:
        self.logger.info("Deploying payload via QEMU guest agent...")
        return {"status": "detonated", "engine": "QEMU"}

    def teardown(self) -> bool:
        if self.process:
            self.process.terminate()
        self.is_running = False
        return True
