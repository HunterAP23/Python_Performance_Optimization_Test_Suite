import functools as ft

cimport cython  # noqa: E999


@cython.cfunc
@cython.returns(list)
@cython.locals(i=cython.int)
def is_prime(n: cython.int, primes: (cython.int,...), boundary: cython.int) -> list:
    return [ft.lru_cache(maxsize=None)(n % i for i in primes if i <= boundary)]
