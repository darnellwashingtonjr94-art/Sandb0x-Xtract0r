import subprocess
from sandboxes.base import BaseSandbox

class RedroidRunner(BaseSandbox):
    """Runner for Redroid (Android in Docker)."""
    
    def __init__(self, sandbox_id: str, port: int = 5555):
        super().__init__(sandbox_id, "Android-Container")
        self.port = port
        self.container_name = f"redroid_{self.sandbox_id}"

    def provision(self) -> bool:
        self.logger.info("Pulling Redroid image...")
        return True

    def start(self) -> bool:
        subprocess.run([
            "docker", "run", "-d", "--rm", "--privileged",
            "-v", "~/data:/data",
            "-p", f"{self.port}:5555",
            "--name", self.container_name,
            "redroid/redroid:11.0.0-latest"
        ])
        self.is_running = True
        return True

    def detonate(self, payload_path: str) -> dict:
        self.logger.info("Connecting ADB to Redroid container...")
        subprocess.run(["adb", "connect", f"localhost:{self.port}"])
        return {"status": "detonated", "engine": "Redroid"}

    def teardown(self) -> bool:
        subprocess.run(["docker", "stop", self.container_name])
        self.is_running = False
        return True
