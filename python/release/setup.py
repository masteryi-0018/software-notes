print("setup.py loaded")

from setuptools import setup

setup(
    name="hello_pkg",
    version="0.1",
    description="A simple hello package",
    author="masteryi",
    packages=["hello_pkg"],
)
