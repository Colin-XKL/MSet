#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name="Mset",
    version=0.1,
    description=("A tool for quickly set mirror for apt/yum/pip/npm..."),
    long_description=open("README.md").read(),
    author="Colin",
    author_email="Colin_XKL@outlook.com",
    maintainer="Colin",
    maintainer_email="Colin_XKL@outlook.com",
    license="MIT License",
    packages=find_packages(),
    platforms=["all"],
    url="https://github.com/Colin-XKL/MSet",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
)
