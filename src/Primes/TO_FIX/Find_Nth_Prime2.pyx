cimport cython
import datetime as dt
import decimal
import functools as ft
import math
import numbers
import time

table = []
table2 = []
table3 = []


def print_lock(msg, rlock):
    rlock.acquire()
    print(msg)
    rlock.release()


def is_prime(num):
    global table
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        for i in range(len(table)):
            checks = checks + 1
            if num % table[i] == 0:
                return [False, checks]
            else:
                continue
        table.append(num)
        return [True, checks]


def is_prime_half(num):
    global table2
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        boundary = math.floor(num / 2)
        for i in range(len(table2)):
            if table[i] <= boundary:
                checks = checks + 1
                if num % table[i] == 0:
                    return [False, checks]
                else:
                    continue
        table2.append(num)
        return [True, checks]


def is_prime_sqrt(num):
    global table3
    checks = 0

    if num <= 1:
        return [False, 0]
    else:
        checks = checks + 1
        boundary = int(math.floor(math.sqrt(num)))
        for i in range(len(table3)):
            if table[i] <= boundary:
                checks = checks + 1
                if num % table[i] == 0:
                    return [False, checks]
                else:
                    continue
        table3.append(num)
        return [True, checks]


def main_def(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Default started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_default_time.txt"
    my_file2 = "files_runs/optimized_default_divisions.txt"
    txt_output = open(my_file, "a")
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(my_max):
            tmp = is_prime(j)
            if tmp[0] == True:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Default Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in divisions_list:
        txt_output2.write(item)
    txt_output2.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Default Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)

    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    txt_output.write("Average time it took to calculate {0} optimized normal passes was {1} seconds.".format(num_loops, average_time))
    txt_output.close()


def main_half(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Half started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_half_time.txt"
    my_file2 = "files_runs/optimized_half_division.txt"
    txt_output = open(my_file, "a")
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(my_max):
            tmp = is_prime_half(j)
            if tmp[0] == True:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Half Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in divisions_list:
        txt_output2.write(item)
    txt_output2.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Half Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)

    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    txt_output.write("Average time it took to calculate {0} optimized half-bound passes was {1} seconds.".format(num_loops, average_time))
    txt_output.close()


def main_sqrt(int my_max, int num_loops, rlock):
    msg = ("-" * 80) + "\n"
    msg += "Optimized Sqrt started."
    print_lock(msg, rlock)

    my_file = "files_runs/optimized_sqrt_time.txt"
    my_file2 = "files_runs/optimized_sqrt_divisions.txt"
    txt_output = open(my_file, "a")
    txt_output2 = open(my_file2, "a")
    time_list = []
    divisions_list = []

    for i in range(num_loops):
        tmp_time_start = time.time()
        table = []
        for i in range(my_max):
            tmp = is_prime_sqrt(j)
            if tmp[0] == True:
                divisions_list.append("{0} took {1} divisions by previous primes to complete!\n\n".format(i, tmp[1]))

        tmp_time_total = time.time() - tmp_time_start

        txt_output.write("Optimized Sqrt Pass {0} took {1} seconds.\n".format(i + 1, tmp_time_total))
        time_list.append(tmp_time_total)

    for item in divisions_list:
        txt_output2.write(item)
    txt_output2.close()

    time_now = dt.datetime.now()
    msg = ("-" * 80) + "\n"
    msg += "Optimized Sqrt Finished at {0}/{1}/{2} {3}:{4}:{5}:{6}".format(time_now.year, time_now.month, time_now.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)

    print_lock(msg, rlock)

    average_time = ft.reduce(lambda a, b: a + b, time_list) / len(time_list)
    txt_output.write("Average time it took to calculate {0} optimized sqrt-bound passes was {1} seconds.".format(num_loops, average_time))
    txt_output.close()