from setuptools import setup, find_packages


setup(
    name="HelloJelly",
    version="1.0.1",
    packages=find_packages(exclude=["test", "integration_test"])
)
