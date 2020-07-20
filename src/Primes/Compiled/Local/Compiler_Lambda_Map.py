from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Local.Lambda_Map", ["Primes/Compiled/Local/Lambda_Map.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)