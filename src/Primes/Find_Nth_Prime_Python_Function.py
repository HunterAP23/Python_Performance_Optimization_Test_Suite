import datetime as dt
import functools as ft
import math
import time


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime(n, table):
    checks = 0

    if n <= 1:
        checks = 1
        return (False, checks)
    else:
        if len(table) == 0:
            for i in range(2, n):
                if n % table[i] == 0:
                    return (False, checks)
                else:
                    checks += 1
        else:
            for i in range(len(table)):
                if n % table[i] == 0:
                    return (False, checks)
                else:
                    checks += 1
        return (True, checks)


def is_prime_half(n, table):
    checks = 0

    if n <= 1:
        checks = 1
        return (False, checks)
    else:
        boundary = math.floor(n / 2)
        for i in range(len(table)):
            if table[i] <= boundary:
                if n % table[i] == 0:
                    return (False, checks)
                else:
                    checks += 1
            else:
                break
        return (True, checks)


def is_prime_sqrt(n, table):
    checks = 0

    if n <= 1:
        checks = 1
        return (False, checks)
    else:
        boundary = math.floor(math.sqrt(n))
        for i in range(len(table)):
            if table[i] <= boundary:
                if n % table[i] == 0:
                    return (False, checks)
                else:
                    checks += 1
            else:
                break
        return (True, checks)


def main_def(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Default (Function) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/normal_function/default_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []

        tmp_time_start = time.time()
        for i in range(2, my_max):
            tmp = is_prime(i, primes_list)
            if tmp[0]:
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(i, tmp[1]))
                primes_list.append(i)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Default (Function) Pass {0} took {1} seconds.\n\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/normal_function/default_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/normal_function/default_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Default (Function) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal default (Function) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def main_half(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Half (Function) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/normal_function/half_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []

        tmp_time_start = time.time()
        for i in range(2, my_max):
            tmp = is_prime_half(i, primes_list)
            if tmp[0]:
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(i, tmp[1]))
                primes_list.append(i)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Half (Function) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/normal_function/half_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/normal_function/half_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Half (Function) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal half-bound (Function) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()


def main_sqrt(my_max, num_loops, rlock):
    msg = ("-" * 80) + "\n"
    overall_start = dt.datetime.now()
    msg += "Normal Sqrt (Function) started at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(overall_start.year, overall_start.month, overall_start.day, overall_start.hour, overall_start.minute, overall_start.second, overall_start.microsecond)
    print_lock(msg, rlock)

    time_list = []
    div_list = []
    primes_list = []

    time_output = open("files_runs/normal_function/sqrt_time.txt", "w")

    for i in range(num_loops):
        # Clear the lists before a run
        time_list = []
        div_list = []
        primes_list = []

        tmp_time_start = time.time()
        for i in range(2, my_max):
            tmp = is_prime_sqrt(i, primes_list)
            if tmp[0]:
                div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(i, tmp[1]))
                primes_list.append(i)

        tmp_time_total = time.time() - tmp_time_start

        time_output.write("Normal Sqrt (Function) Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    with open("files_runs/normal_function/sqrt_divisions.txt", "w") as div_output:
        for div in div_list:
            div_output.write(div)

    with open("files_runs/normal_function/sqrt_primes.txt", "w") as primes_output:
        for prime in primes_list:
            primes_output.write("{0}\n".format(prime))

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Normal Sqrt (Function) Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    msg = "Average time it took to calculate {0} normal sqrt-bound (Function) passes was {1} seconds.".format(num_loops, average_time)
    time_output.write(msg)
    print_lock(msg, rlock)
    time_output.close()