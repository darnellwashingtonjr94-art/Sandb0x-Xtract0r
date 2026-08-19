"""
S@ndb0x-Xtract0r Multi-LLM Bot Package
Integrates Google Gemini, Anthropic Claude, and OpenAI ChatGPT/Codex.
"""

from .gateway import MultiLLMGateway
from .prompts import SYSTEM_PROMPTS
from .synthesizer import TelemetrySynthesizer

__all__ = ["MultiLLMGateway", "SYSTEM_PROMPTS", "TelemetrySynthesizer"]
