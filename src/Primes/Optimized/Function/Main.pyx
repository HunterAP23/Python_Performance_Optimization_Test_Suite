import importlib
import math
import time

cimport cython  # noqa: E999


@cython.ccall
def Main(value_max: cython.int, num_loops: cython.int, bounding: str, runtime: str, compilation: str, call_type: str, subcall: str) -> dict:
    return Main_Sub(value_max, num_loops, bounding, runtime, compilation, call_type, subcall)


@cython.cfunc
@cython.returns(dict)
@cython.locals(i=cython.int, ret=list, j=cython.int, tmp_time_start=cython.double, tmp_time_end=cython.double)
def Main_Sub(value_max: cython.int, num_loops: cython.int, bounding: str, runtime: str, compilation: str, call_type: str, subcall: str) -> dict:
    cdef str package = ".".join(["Primes", compilation, call_type, subcall])
    lib = importlib.import_module(package)
    func = vars(lib)["is_prime"]

    cdef dict data = {
        "divisions": dict(),
        "primes": dict(),
        "times": dict(),
    }
    cdef int n
    cdef int boundary

    for i in range(num_loops):
        data["divisions"][i] = dict()
        data["times"][i] = []
        data["primes"][i] = []
        data["primes"][i].append(2)

        for n in range(3, value_max, 2):
            ret = []
            tmp_time_start = time.perf_counter()
            boundary = n
            if bounding == "Half":
                boundary = math.floor(n / 2)
            elif bounding == "Sqrt":
                boundary = math.floor(math.sqrt(n))
            if "generator" in subcall.lower():
                ret = list(func(n, data["primes"][i], boundary))
            else:
                ret = func(n, data["primes"][i], boundary)
            tmp_time_end = time.perf_counter()
            data["times"][i].append(tmp_time_end - tmp_time_start)

            data["divisions"][i][n] = len(ret)
            if all(ret):
                data["primes"][i].append(n)

    return data