# Scripts & Automation (`/scripts`)

This folder contains utility scripts for environment setup, payload encryption, and CI/CD orchestration.

## Available Utilities

| Script | Purpose | Execution Context |
|---|---|---|
| `setup.sh` | Installs system dependencies (Mingw-w64, Python requirements). | Host OS (Linux/macOS) |
| `encrypt_payload.py` | Encrypts raw binaries to bypass static disk signatures. | Build Pipeline |
| `generate_cert.sh` | Creates self-signed certificates for signing the compiled executables. | Post-Build |
| `clean_workspace.sh` | Wipes all compiled objects, `.enc` files, and logs. | Pre-Commit |

## CI/CD Integration
If integrating with GitHub Actions, the workflow YAML will call `scripts/setup.sh` followed by standard `make` commands. Ensure the runner environments support cross-compilation if targeting Windows from a Linux runner.
