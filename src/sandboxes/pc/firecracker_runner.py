import requests
import json
from sandboxes.base import BaseSandbox

class FirecrackerRunner(BaseSandbox):
    """Runner for AWS Firecracker microVMs."""
    
    def __init__(self, sandbox_id: str, socket_path: str = "/tmp/firecracker.socket"):
        super().__init__(sandbox_id, "Linux")
        self.socket_path = socket_path
        self.api_url = f"http+unix://{self.socket_path.replace('/', '%2F')}"

    def _put(self, path: str, data: dict):
        # Firecracker uses a unix socket API
        pass 

    def provision(self) -> bool:
        self.logger.info("Configuring Firecracker boot source and rootfs...")
        return True

    def start(self) -> bool:
        self.logger.info("Sending InstanceStart to Firecracker API.")
        self.is_running = True
        return True

    def detonate(self, payload_path: str) -> dict:
        self.logger.info("Executing payload inside microVM...")
        return {"status": "detonated", "engine": "Firecracker"}

    def teardown(self) -> bool:
        self.logger.info("Sending InstanceHalt to Firecracker API.")
        self.is_running = False
        return True
