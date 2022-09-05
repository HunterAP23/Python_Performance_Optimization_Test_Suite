import functools as ft


@ft.lru_cache(maxsize=None)
def is_prime(n: int, primes: tuple, boundary: int) -> list:
    ret = []
    for i in primes:
        if i <= boundary:
            ret.append(ft.lru_cache(maxsize=None)(lambda y: n % y)(i))
        else:
            break
    return ret
