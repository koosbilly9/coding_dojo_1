# python -m pip install -e .
from setuptools import setup, find_packages

setup(
    name="some_program",
    version="0.0.1.1",
    packages=find_packages(exclude=["test"]),
    install_requires=[
        "certifi"
    ]
)