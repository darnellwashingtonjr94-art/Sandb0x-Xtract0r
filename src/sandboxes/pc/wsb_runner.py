import os
import subprocess
from pathlib import Path
from sandboxes.base import BaseSandbox

class WSBRunner(BaseSandbox):
    """Runner for native Windows Sandbox API (.wsb)."""
    
    def __init__(self, sandbox_id: str):
        super().__init__(sandbox_id, "Windows")
        self.wsb_path = f"/tmp/{self.sandbox_id}.wsb"

    def provision(self) -> bool:
        wsb_config = f"""
        <Configuration>
            <Networking>Default</Networking>
            <MappedFolders>
                <MappedFolder>
                    <HostFolder>{os.getcwd()}/shared_payloads</HostFolder>
                    <SandboxFolder>C:\\Payloads</SandboxFolder>
                    <ReadOnly>true</ReadOnly>
                </MappedFolder>
            </MappedFolders>
            <LogonCommand>
                <Command>explorer.exe C:\\Payloads</Command>
            </LogonCommand>
        </Configuration>
        """
        Path(self.wsb_path).write_text(wsb_config)
        self.logger.info("Windows Sandbox configuration generated.")
        return True

    def start(self) -> bool:
        subprocess.Popen(["cmd.exe", "/c", self.wsb_path])
        self.is_running = True
        return True

    def detonate(self, payload_path: str) -> dict:
        self.logger.info(f"Detonating {payload_path} inside WSB...")
        # WSB telemetry relies on host-level ETW (Event Tracing for Windows)
        return {"status": "detonated", "engine": "WSB"}

    def teardown(self) -> bool:
        if os.path.exists(self.wsb_path):
            os.remove(self.wsb_path)
        self.is_running = False
        return True
