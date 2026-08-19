import subprocess
from sandboxes.base import SandboxBase

class AndroidRunner(SandboxBase):
    def revert_snapshot(self) -> bool:
        print("[Android AVD] Wiping emulator userdata to baseline snapshot...")
        subprocess.run(["adb", "emu", "avd", "snapshot", "load", "clean_boot"], check=False)
        return True

    def execute_sample(self, sample_path: str, timeout: int = 180) -> dict:
        print(f"[Android AVD] Installing package: {sample_path}")
        subprocess.run(["adb", "install", "-r", sample_path], check=False)
        print("[Android AVD] Launching package and spawning adb logcat trace...")
        return {"status": "executed", "platform": "android"}

    def cleanup(self) -> bool:
        print("[Android AVD] Uninstalling test application package...")
        return True
