import argparse
import sys
from orchestrator.router import FileRouter
from orchestrator.scheduler import TaskScheduler
from llm_bot.gateway import MultiLLMGateway
from reporting.markdown_writer import MarkdownReportWriter

def main():
    parser = argparse.ArgumentParser(description="S@ndb0x-Xtract0r CLI Controller")
    parser.add_argument("--file", required=True, help="Path to suspicious binary/package")
    parser.add_argument("--platform", choices=["auto", "windows", "linux", "android", "ios", "container"], default="auto")
    args = parser.parse_args()

    print(f"[*] Initializing S@ndb0x-Xtract0r for sample: {args.file}")
    
    router = FileRouter()
    target_platform = router.detect_platform(args.file) if args.platform == "auto" else args.platform
    print(f"[+] Targeted execution platform: {target_platform}")

    scheduler = TaskScheduler()
    task_id = scheduler.enqueue(args.file, target_platform)
    print(f"[+] Task enqueued successfully. Task ID: {task_id}")

    telemetry = scheduler.run_task(task_id)
    
    print("[*] Dispatching telemetry to Multi-LLM Bot (Gemini, Claude, ChatGPT, Codex)...")
    llm_gateway = MultiLLMGateway()
    analysis_payload = llm_gateway.analyze_telemetry(telemetry)

    writer = MarkdownReportWriter()
    report_path = writer.generate(task_id, telemetry, analysis_payload)
    print(f"[SUCCESS] Report documented and saved to: {report_path}")

if __name__ == "__main__":
    main()
