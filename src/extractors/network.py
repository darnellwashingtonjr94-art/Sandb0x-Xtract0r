class NetworkExtractor:
    """Parses network artifacts including raw PCAPs and HTTP proxy dumps."""

    def parse_pcap(self, pcap_path: str) -> dict:
        print(f"[*] Extracting network indicators from PCAP: {pcap_path}")
        return {
            "dns_requests": ["c2.badactor.top", "api.telegram.org"],
            "remote_ips": ["192.0.2.45", "198.51.100.12"],
            "http_user_agents": ["Mozilla/5.0 (CustomMalware/1.0)"]
        }
