import functools as ft


def is_prime(n: int, primes: tuple, boundary: int) -> list:
    return list(map(ft.lru_cache(maxsize=None)(lambda y: n % y if y <= boundary else 1), primes))