from setuptools import setup, find_packages

setup(
    name="sandb0x-xtractor",  # Replace with your exact PyPI package name (lowercase recommended)
    version="0.1.0",         # Update this version when publishing updates
    author="darnellwashingtonjr94-art",
    description="A heuristic directory scanning and sandboxing security extraction tool",
    long_description=open("README.md", encoding="utf-8").read() if "README.md" in __import__("os").listdir(".") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/darnellwashingtonjr94-art/sandb0x-Xtract0r",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
