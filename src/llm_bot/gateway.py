import os
from google import genai
from anthropic import Anthropic
from openai import OpenAI
from src.llm_bot.prompts import SYSTEM_PROMPTS

class MultiLLMGateway:
    """Unified client gateway querying Gemini, Claude, and ChatGPT/Codex."""

    def __init__(self):
        # API key retrieval from environment
        gemini_key = os.getenv("GOOGLE_API_KEY", "mock_key")
        claude_key = os.getenv("ANTHROPIC_API_KEY", "mock_key")
        openai_key = os.getenv("OPENAI_API_KEY", "mock_key")

        self.gemini_client = genai.Client(api_key=gemini_key) if gemini_key != "mock_key" else None
        self.claude_client = Anthropic(api_key=claude_key) if claude_key != "mock_key" else None
        self.openai_client = OpenAI(api_key=openai_key) if openai_key != "mock_key" else None

    def query_gemini(self, telemetry_summary: str) -> str:
        if not self.gemini_client:
            return "[Gemini Mock] High Severity Threat (8.5/10). Process spawned stealthy powershell and established outbound C2."
        
        prompt = f"{SYSTEM_PROMPTS['gemini']}\n\nTelemetry:\n{telemetry_summary}"
        response = self.gemini_client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )
        return response.text

    def query_claude(self, telemetry_summary: str) -> str:
        if not self.claude_client:
            return "[Claude Mock] MITRE ATT&CK Mapping:\n- T1059.001 (PowerShell)\n- T1547.001 (Registry Run Keys)\n- T1071.001 (Web Protocols)"
        
        prompt = f"{SYSTEM_PROMPTS['claude']}\n\nTelemetry:\n{telemetry_summary}"
        response = self.claude_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    def query_chatgpt_codex(self, telemetry_summary: str) -> str:
        if not self.openai_client:
            return "[ChatGPT/Codex Mock]\nrule Malicious_Payload {\n    strings:\n        $a = \"c2.badactor.top\"\n    condition:\n        $a\n}"
        
        prompt = f"{SYSTEM_PROMPTS['openai']}\n\nTelemetry:\n{telemetry_summary}"
        response = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def analyze_telemetry(self, telemetry: dict) -> dict:
        summary_str = str(telemetry)
        return {
            "gemini": self.query_gemini(summary_str),
            "claude": self.query_claude(summary_str),
            "openai": self.query_chatgpt_codex(summary_str)
        }
