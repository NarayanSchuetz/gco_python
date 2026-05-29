import os
import subprocess

import numpy
from setuptools import Extension, setup
from Cython.Build import cythonize

VERSION = "0.0.1"

# Fetch + checksum-verify the GCO C++ sources (see Makefile). This intentionally
# runs unconditionally: if the download or build deps are missing, the build
# MUST fail rather than silently produce a package without the native module.
subprocess.check_call(["make", "gco_src"])

gco_directory = "gco_src"
sources = [
    "gco_python.pyx",
    os.path.join(gco_directory, "GCoptimization.cpp"),
    os.path.join(gco_directory, "graph.cpp"),
    os.path.join(gco_directory, "LinkedBlockList.cpp"),
    os.path.join(gco_directory, "maxflow.cpp"),
]

setup(
    name="pygco",
    version=VERSION,
    ext_modules=cythonize(
        [
            Extension(
                "pygco",
                sources,
                language="c++",
                include_dirs=[gco_directory, numpy.get_include()],
                library_dirs=[gco_directory],
                extra_compile_args=["-fpermissive"],
            )
        ]
    ),
)
