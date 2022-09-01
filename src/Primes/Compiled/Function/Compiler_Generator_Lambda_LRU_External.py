from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension(
        "Primes.Compiled.Function.Generator_Lambda_LRU_External",
        ["src/Primes/Interpreted/Function/Generator_Lambda_LRU_External.py"],
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
