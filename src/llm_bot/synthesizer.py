class TelemetrySynthesizer:
    """Normalizes and prepares raw multi-source telemetry data for LLM ingest."""

    def format_for_llm(self, task_id: str, raw_telemetry: dict, mem_data: dict, net_data: dict) -> str:
        formatted_output = f"""
=== TASK ID: {task_id} ===
[PROCESS EVENTS]
{raw_telemetry.get('processes', [])}

[NETWORK EVENTS]
{net_data.get('dns_requests', raw_telemetry.get('network', []))}

[FILESYSTEM & REGISTRY]
Modified Files: {raw_telemetry.get('files_modified', [])}
Registry Modifications: {raw_telemetry.get('registry_keys', [])}

[MEMORY INJECTIONS]
{mem_data.get('injected_code', [])}
Suspicious Strings: {mem_data.get('suspicious_strings', [])}
"""
        return formatted_output.strip()
