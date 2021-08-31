#! /usr/bin/env python
import os
import sys

import numpy as np
from setuptools import Extension, find_packages, setup

common_flags = {
    "include_dirs": [
        np.get_include(),
        os.path.join(sys.prefix, "include"),
    ],
    "library_dirs": [],
    "define_macros": [],
    "undef_macros": [],
    "extra_compile_args": [],
    "language": "c++",
}

libraries = []

# Locate directories under Windows %LIBRARY_PREFIX%.
if sys.platform.startswith("win"):
    common_flags["include_dirs"].append(os.path.join(sys.prefix, "Library", "include"))
    common_flags["library_dirs"].append(os.path.join(sys.prefix, "Library", "lib"))

ext_modules = [
    Extension(
        "pymt_heatcxx.lib.heatmodelcxx",
        ["pymt_heatcxx/lib/heatmodelcxx.pyx"],
        libraries=libraries + ["bmiheatcxx"],
        **common_flags
    ),
]

entry_points = {
    "pymt.plugins": [
        "HeatModelCxx=pymt_heatcxx.bmi:HeatModelCxx",
    ]
}


def read(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read()


long_description = u"\n\n".join(
    [read("README.rst"), read("CREDITS.rst"), read("CHANGES.rst")]
)


setup(
    name="pymt_heatcxx",
    author="csdms",
    author_email="csdms@colorado.edu",
    description="PyMT plugin for pymt_heatcxx",
    long_description=long_description,
    version="0.2.dev0",
    url="https://github.com/pymt-lab/pymt_heatcxx",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["bmi", "pymt"],
    install_requires=open("requirements.txt", "r").read().splitlines(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=find_packages(),
    entry_points=entry_points,
    include_package_data=True,
)
