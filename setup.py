from setuptools import setup
from pathlib import Path

setup(
    name="micro-process",
    version="1.0",
    description="modules for create a python sub-process",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    url="https://github.com/MisterMine01/MicroProcess",
    author="MisterMine01",
    py_modules=['micro_process'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
    keywords=["sub-process", "execution"]
)
