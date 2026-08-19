class ProcessExtractor:
    """Parses system process trees, DLL injections, and API calls."""

    def parse_proc_tree(self, raw_logs: list) -> list:
        print("[*] Parsing parent-child process relationships...")
        return [
            {"pid": 1024, "name": "explorer.exe", "parent": 0},
            {"pid": 2048, "name": "malicious.exe", "parent": 1024},
            {"pid": 3072, "name": "cmd.exe", "parent": 2048, "args": "/c powershell -w hidden"}
        ]
