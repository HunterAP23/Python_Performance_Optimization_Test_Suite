import functools as ft
import math


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime_default(n: int, table: list):
    checks = 0

    for i in range(len(table)):
        if n % table[i] == 0:
            return (False, 1)
        else:
            checks += 1
    return (True, checks)


@ft.lru_cache(maxsize=None)
def is_prime_half(n: int, table: list):
    checks = 0

    boundary = math.floor(n / 2)
    for i in range(len(table)):
        if table[i] <= boundary:
            if n % table[i] == 0:
                return (False, 1)
            else:
                checks += 1
        else:
            break
    return (True, checks)


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n: int, table: list):
    checks = 0

    boundary = math.floor(math.sqrt(n))
    for i in range(len(table)):
        if table[i] <= boundary:
            if n % table[i] == 0:
                return (False, 1)
            else:
                checks += 1
        else:
            break
    return (True, checks)