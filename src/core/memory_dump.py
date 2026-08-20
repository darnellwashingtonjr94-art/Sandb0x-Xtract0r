import subprocess
from pathlib import Path

def dump_memory_qemu(vm_name: str, output_path: str):
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    
    cmd = ["virsh", "dump", vm_name, str(out), "--memory-only"]
    subprocess.run(cmd, check=True)
    print(f"[+] Memory dump saved successfully to {out}")
