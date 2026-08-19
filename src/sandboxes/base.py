from abc import ABC, abstractmethod
import logging

class BaseSandbox(ABC):
    """Abstract base class for Sandb0x-Xtract0r runners."""
    
    def __init__(self, sandbox_id: str, platform: str):
        self.sandbox_id = sandbox_id
        self.platform = platform
        self.is_running = False
        self.telemetry = {}
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(f"Sandbox-{self.sandbox_id}")

    @abstractmethod
    def provision(self) -> bool:
        """Initialize and configure the isolated environment."""
        pass

    @abstractmethod
    def start(self) -> bool:
        """Boot the sandbox and begin environment monitoring."""
        pass

    @abstractmethod
    def detonate(self, payload_path: str) -> dict:
        """Execute the payload and capture process/network traces."""
        pass

    @abstractmethod
    def teardown(self) -> bool:
        """Destroy the environment and wipe artifacts."""
        pass
