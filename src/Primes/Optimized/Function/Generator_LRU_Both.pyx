import functools as ft

cimport cython  # noqa: E999


# ! Can not compile generator functions with cdef / cfunc
@cython.locals(i=cython.int)
@ft.lru_cache(maxsize=None)
def is_prime(n: cython.int, primes: (cython.int,...), boundary: cython.int):
    for i in primes:
        if i < boundary:
            yield ft.lru_cache(maxsize=None)(n % i)
        else:
            break
