from setuptools import setup, find_packages

setup(
    name="sandb0x-xtractor",  # MUST match your PyPI project name exactly
    version="0.1.1",         # Update version if needed
    author="darnellwashingtonjr94-art",
    description="An automated cross-platform security analysis engine",
    long_description=open("README.md", encoding="utf-8").read() if "README.md" in __import__("os").listdir(".") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/darnellwashingtonjr94-art/Sandb0x-Xtract0r",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
