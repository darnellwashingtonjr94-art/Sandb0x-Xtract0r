import os
import magic

class FileRouter:
    """Inspects file extension and magic bytes to route payload to runner platform."""

    def detect_platform(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Target sample not found: {file_path}")

        ext = os.path.splitext(file_path)[1].lower()

        # Check explicit file extension overrides first
        if ext == ".apk":
            return "android"
        elif ext in [".ipa", ".deb"]:
            return "ios"
        elif ext in [".exe", ".dll", ".sys"]:
            return "windows"

        # Inspect file magic bytes
        file_type = magic.from_file(file_path).lower()

        if "pe32" in file_type:
            return "windows"
        elif "elf" in file_type or ext in [".so", ".bin"]:
            return "linux"
        elif "zip" in file_type and ext == ".apk":
            return "android"
        elif ext in [".sh", ".py", ".yaml"] or "docker" in file_type:
            return "container"

        return "windows"  # Default fallback
