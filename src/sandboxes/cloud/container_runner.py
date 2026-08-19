import subprocess
from sandboxes.base import BaseSandbox

class ContainerRunner(BaseSandbox):
    """Runner for Cloud environments using gVisor/Kata."""
    
    def __init__(self, sandbox_id: str, runtime: str = "runsc"):
        super().__init__(sandbox_id, "Cloud")
        self.runtime = runtime # 'runsc' for gVisor, 'kata-runtime' for Kata
        self.container_name = f"sandbox_{self.sandbox_id}"

    def provision(self) -> bool:
        self.logger.info(f"Preparing container with {self.runtime} runtime.")
        return True

    def start(self) -> bool:
        subprocess.run([
            "docker", "run", "-d", "--rm",
            "--runtime", self.runtime,
            "--name", self.container_name,
            "ubuntu:latest", "sleep", "infinity"
        ])
        self.is_running = True
        return True

    def detonate(self, payload_path: str) -> dict:
        self.logger.info(f"Copying {payload_path} and executing in gVisor sandbox...")
        subprocess.run(["docker", "cp", payload_path, f"{self.container_name}:/tmp/payload"])
        subprocess.run(["docker", "exec", self.container_name, "/tmp/payload"])
        return {"status": "detonated", "engine": "Container"}

    def teardown(self) -> bool:
        subprocess.run(["docker", "stop", self.container_name])
        self.is_running = False
        return True
