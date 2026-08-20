# Source Directory (`/src`)

This directory contains the core engine components for Sandb0x-Xtract0r. The architecture is modular, allowing for independent compilation of evasion techniques and payload handlers.

## Module Breakdown

### 1. `evasion/`
Contains heuristics for environment detection:
* `cpu_checks.c`: Validates CPU core counts and temperature sensors (often spoofed or static in VMs).
* `mac_oui.c`: Checks host MAC addresses against known hypervisor vendor blocklists.
* `timing.c`: Implements RDTSC checks to detect time distortion caused by debuggers or virtualization.

### 2. `loader/`
Handles in-memory execution of the final payload post-validation:
* `reflective_dll.c`: Custom Reflective DLL injection logic.
* `syscalls.asm`: Direct system calls to bypass user-land API hooking (e.g., `ntdll.dll` hooks).

### Build Instructions
Do not compile directly from this directory. Use the root `Makefile` to ensure proper linking and obfuscation flags are applied.
