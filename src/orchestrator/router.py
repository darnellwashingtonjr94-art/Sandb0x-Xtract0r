import os
import filetype

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

        # Inspect file magic bytes using pure Python filetype
        kind = filetype.guess(file_path)
        file_type = f"{kind.mime} {kind.extension}".lower() if kind else ""

        if "exe" in file_type or "dll" in file_type or "pe32" in file_type:
            return "windows"
        elif "elf" in file_type or "bin" in file_type:
            return "linux"
        elif "zip" in file_type or ext == ".apk":
            return "android"
        elif "tar" in file_type or "json" in file_type or "yaml" in file_type:
            return "container"

        return "windows"  # Default fallback
