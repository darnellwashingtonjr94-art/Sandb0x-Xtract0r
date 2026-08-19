import unittest
from src.llm_bot.gateway import MultiLLMGateway
from src.llm_bot.synthesizer import TelemetrySynthesizer

class TestLLMBot(unittest.TestCase):
    def test_synthesizer_formatting(self):
        synth = TelemetrySynthesizer()
        output = synth.format_for_llm(
            task_id="task_123",
            raw_telemetry={"processes": ["cmd.exe"]},
            mem_data={"injected_code": []},
            net_data={"dns_requests": ["example.com"]}
        )
        self.assertIn("TASK ID: task_123", output)
        self.assertIn("example.com", output)

    def test_gateway_mock_fallback(self):
        gateway = MultiLLMGateway()
        res = gateway.analyze_telemetry({"test": "data"})
        self.assertIn("gemini", res)
        self.assertIn("claude", res)
        self.assertIn("openai", res)

if __name__ == "__main__":
    unittest.main()
