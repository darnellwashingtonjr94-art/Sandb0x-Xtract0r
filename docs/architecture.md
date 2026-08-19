# S@ndb0x-Xtract0r System Architecture

## Core Components

1. **Ingest & Routing Gateway:** Accepts raw payload submissions via CLI or FastAPI endpoint (`/api/v1/submit`), inspects binary headers (`python-magic`), and routes to the corresponding execution profile.
2. **Sandbox Execution Engine:** Implements the `SandboxBase` interface for cross-platform isolation:
   - **PC:** QEMU/KVM virtual machines for Windows/Linux.
   - **Mobile:** Android AVD and Corellium iOS cloud instances.
   - **Cloud:** Docker containers instrumented with eBPF probes.
3. **Telemetry Extractors:** Isolates runtime artifacts during execution (Network PCAPs, Volatility RAM dumps, Process trees, eBPF logs).
4. **Multi-LLM Bot:** Integrates Google Gemini (fast triage), Anthropic Claude (MITRE ATT&CK breakdown), and OpenAI ChatGPT/Codex (YARA rule & exploit code generation).
5. **Reporting Pipeline:** Compiles multi-model outputs into clean Markdown and PDF files saved under `storage/reports/`.
