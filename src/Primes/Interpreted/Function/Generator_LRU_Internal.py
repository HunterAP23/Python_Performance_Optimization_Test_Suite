import functools as ft

from PO_Standard import measure_resources


@measure_resources
def is_prime(n: int, primes: tuple, boundary: int):
    for i in primes:
        if i < boundary:
            yield ft.lru_cache(maxsize=None)(n % i)
        else:
            break
