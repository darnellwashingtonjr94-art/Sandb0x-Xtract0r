<p align="center">
  <img src="IMG_1220.png" alt="Sandb0x-Xtract0r Logo" width="600">
</p>

# Sandb0x-Xtract0r

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://github.com/credkellarboop/Sandb0x-Xtract0r)
[![React](https://img.shields.io/badge/React-UI-61DAFB?logo=react&logoColor=black)](https://github.com/credkellarboop/Sandb0x-Xtract0r)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://github.com/credkellarboop/Sandb0x-Xtract0r)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)](https://github.com/credkellarboop/Sandb0x-Xtract0r)
[![Redis](https://img.shields.io/badge/Redis-Task_Broker-DC382D?logo=redis&logoColor=white)](https://github.com/credkellarboop/Sandb0x-Xtract0r)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?logo=tailwind-css&logoColor=white)](https://github.com/credkellarboop/Sandb0x-Xtract0r)
[![AI Engine](https://img.shields.io/badge/AI_Engine-Gemini_|_Claude_|_OpenAI-9cf?logo=openai&logoColor=white)](https://github.com/credkellarboop/Sandb0x-Xtract0r)
[![CI/CD](https://github.com/credkellarboop/Sandb0x-Xtract0r/actions/workflows/test.yml/badge.svg)](https://github.com/credkellarboop/Sandb0x-Xtract0r/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## What is this?
**Sandb0x-Xtract0r** is an automated, cross-platform security analysis engine. It provides a unified environment to safely detonate suspicious files, binaries, and applications across PC, mobile, and cloud environments. While the payload executes, the system captures runtime telemetry, network traces, and memory dumps, which are then synthesized into structured threat reports by an integrated multi-LLM bot.

## Explain this in 5th grade reading please
Imagine you find a mystery package on your porch, but you aren't sure if it's a cool toy or a messy glitter bomb. 

Instead of opening it in your living room, you put the package inside a thick, clear plastic box in your backyard. You use robotic arms to open it while cameras record exactly what happens. If it explodes, the mess stays completely trapped in the box, and your house is safe! 

**Sandb0x-Xtract0r** is that clear plastic box, but for computer files. When you find a mystery file, this program puts it inside a fake, trapped computer (the plastic box) and opens it. It watches everything the file does, takes notes, and then has a super-smart robot read the notes to tell you exactly how dangerous the mystery file was.

## What this does?
* **Dynamic Detonation:** Safely executes malware, scripts, and applications targeting Windows, Linux, Android, iOS, and cloud containers.
* **Deep Telemetry Extraction:** Monitors and captures real-time system calls (via eBPF), network traffic (PCAPs), filesystem modifications, and RAM artifacts (memory dumping).
* **AI-Powered Synthesis:** Feeds raw execution telemetry into a multi-LLM gateway (utilizing Gemini, Claude, and OpenAI) to translate complex hexadecimal and machine-level behaviors into readable, MITRE ATT&CK-mapped threat intelligence reports.
* **Automated Orchestration:** Uses a Celery and Redis task queue to manage multiple sandbox environments concurrently without bottlenecking the main API.

## How does this works?
1. **Submission:** A user uploads a suspicious file via the React-based frontend UI or directly through the FastAPI endpoint.
2. **File Routing:** The Orchestrator inspects the file's magic bytes to automatically detect the target platform (e.g., routing an APK to the Redroid Android emulator, or an ELF file to a Linux Firecracker microVM).
3. **Execution & Tracing:** The payload is injected into the highly isolated sandbox. Hooks record API calls, network requests, and spawned processes.
4. **Data Normalization:** Once the execution times out or completes, the Extractor module pulls the raw data (PCAPs, memory strings, registry edits) and normalizes it.
5. **LLM Analysis:** The normalized telemetry is sent to the `llm_bot`, which queries the configured AI models to write a comprehensive security assessment.
6. **Reporting:** The user receives a detailed Markdown or PDF report detailing the payload's intent, lateral movement, and C2 (Command and Control) activity.

## What problems this solves?
* **Platform Fragmentation:** Security researchers usually need entirely different toolchains to analyze an Android APK versus a Windows executable. Sandb0x-Xtract0r centralizes all analysis into one pipeline.
* **Information Overload:** Sifting through thousands of lines of raw system calls and unreadable memory dumps is exhausting. The multi-LLM integration does the heavy lifting, instantly surfacing the most critical threats.
* **Infrastructure Management:** Automatically spins up, resets, and tears down virtualization environments (QEMU, Redroid, Corellium) for every single run, ensuring a clean slate and preventing cross-contamination.

## Why is this so cool?
It bridges the gap between low-level kernel tracing and high-level artificial intelligence. By combining hardware virtualization, modern eBPF tracing, and the latest reasoning capabilities of models like Claude 3.5 Sonnet and Gemini 1.5 Pro, Sandb0x-Xtract0r acts as an automated, highly-scalable junior malware analyst that never needs to sleep.

## How to install this?

**Prerequisites:** Docker, Docker Compose, and a Linux host (recommended for KVM/hardware acceleration).

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/credkellarboop/Sandb0x-Xtract0r.git](https://github.com/credkellarboop/Sandb0x-Xtract0r.git)
   cd Sandb0x-Xtract0r
