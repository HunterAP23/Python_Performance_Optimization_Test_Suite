from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension("Primes.Compiled.Function.List_Lambda_Map", ["src/Primes/Interpreted/Function/List_Lambda_Map.py"])
]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
