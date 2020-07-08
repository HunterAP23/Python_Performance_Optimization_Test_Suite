import datetime as dt
import functools as ft
import math
import time


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


@ft.lru_cache(maxsize=None)
def is_prime(n, table):
    my_lam = ft.lru_cache()(lambda y: n % y)
    ret = []
    for i in range(len(table)):
        ret.append(my_lam(table[i]))
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


@ft.lru_cache(maxsize=None)
def is_prime_half(n, table):
    boundary = math.floor(n / 2)
    my_lam = ft.lru_cache()(lambda y: n % y)
    ret = []
    for i in range(len(table)):
        if table[i] <= boundary:
            ret.append(my_lam(table[i]))
        else:
            break
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


@ft.lru_cache(maxsize=None)
def is_prime_sqrt(n, table):
    boundary = math.floor(math.sqrt(n))
    my_lam = ft.lru_cache()(lambda y: n % y)
    ret = []
    for i in range(len(table)):
        if table[i] <= boundary:
            ret.append(my_lam(table[i]))
        else:
            break
    # return (all(ret), sum([bool(i) for i in ret]))
    return (all(ret), lambda x, y: sum(bool(x), bool(y)), ret)


def main_def(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Default (Function Lambda LRU) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/normal_function_lambda_lru/default_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            tmp = is_prime(n, tuple(primes_list))
            if tmp[0]:
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, tmp[1]))
                primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Default (Function Lambda LRU) Pass {0} took {1} seconds.\n\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/normal_function_lambda_lru/default_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/normal_function_lambda_lru/default_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default (Function Lambda LRU) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal default (Function Lambda LRU) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def main_half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Half (Function Lambda LRU) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/normal_function_lambda_lru/half_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            tmp = is_prime_half(n, tuple(primes_list))
            if tmp[0]:
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, tmp[1]))
                primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Half (Function Lambda LRU) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/normal_function_lambda_lru/half_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/normal_function_lambda_lru/half_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half (Function Lambda LRU) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half-bound (Function Lambda LRU) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def main_sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Sqrt (Function Lambda LRU) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/normal_function_lambda_lru/sqrt_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []
        primes_list.append(2)

        tmp_time_start = time.time()
        for n in range(3, my_max, 2):
            tmp = is_prime_sqrt(n, tuple(primes_list))
            if tmp[0]:
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(n, tmp[1]))
                primes_list.append(n)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Sqrt (Function Lambda LRU) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/normal_function_lambda_lru/sqrt_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/normal_function_lambda_lru/sqrt_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt (Function Lambda LRU) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal sqrt-bound (Function Lambda LRU) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()