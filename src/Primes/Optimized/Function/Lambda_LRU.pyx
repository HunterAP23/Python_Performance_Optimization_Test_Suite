import datetime as dt
import functools as ft
import math
import time
cimport cython


cdef void print_lock(str msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


cdef(bint, int) is_prime_default(int n, list table):
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    cdef list ret = []
    cdef int i
    for i in table:
        ret.append(my_lam(i))
    return (all(ret), sum(ret),)


cdef(bint, int) is_prime_half(int n, list table):
    cdef int boundary = math.floor(n / 2)
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    cdef list ret = []
    cdef int i
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return (all(ret), sum(ret),)


cdef(bint, int) is_prime_sqrt(int n, list table):
    cdef int boundary = math.floor(math.sqrt(n))
    my_lam = ft.lru_cache(maxsize=None)(lambda y: n % y)
    cdef list ret = []
    cdef int i
    for i in table:
        if i <= boundary:
            ret.append(my_lam(i))
        else:
            break
    return (all(ret), sum(ret),)


cpdef void Main(int value_max, int num_loops, rlock, str runtime, str compilation, str call_type, str subcall, str case):
    Main_Sub(value_max, num_loops, rlock, runtime, compilation, call_type, subcall, case)


cdef void Main_Sub(int value_max, int num_loops, rlock, str runtime, str compilation, str call_type, str subcall, str case):
    cdef str group = " ".join([runtime, compilation, call_type, subcall])
    cdef str msg = str(("-" * 80) + "\n")
    overall_start = dt.datetime.now()
    msg += "{0} {1} started at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(group, case, overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_output = open("files_runs/{0}/time_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w")

    func = globals()["is_prime_{0}".format(case.lower())]

    cdef list time_list
    cdef list div_list
    cdef list primes_list
    cdef int i
    cdef int n
    cdef tuple ret
    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, value_max, 2):
            ret = func(n, primes_list)

            if ret[0]:
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, ret[1]))
                primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("{0} {1} Pass {2} took {3} seconds.\n\n".format(group, case, i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    cdef str div
    with open("files_runs/{0}/divisions_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w") as div_output:
        for div in div_list:
            div_output.write(div)

    cdef str prime
    with open("files_runs/{0}/primes_{1}.txt".format(group.replace(" ", "_"), case).lower(), "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = str(("-" * 80) + "\n")
    msg += "{0} {1} finished at {2}/{3}/{4} {5}:{6}:{7}:{8}".format(group, case, time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    cdef double average_time = math.fsum(time_list)
    msg = "Average time it took to calculate {0} passes of {1} {2} was {3} seconds.".format(num_loops, group, case, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()
