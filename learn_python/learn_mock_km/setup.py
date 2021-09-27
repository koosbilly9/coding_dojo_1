from setuptools import setup, find_packages

setup(
    name="myEgg",
    version="0.0.1.1",
    packages=find_packages(exclude=["test"]),
    install_requires=[
        "pcs-common",
        "pcs-telegram",
        "pcs-telegram-definitions",
    ]
)
