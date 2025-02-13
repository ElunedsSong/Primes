import math
import sympy
import numpy


def prime_factors_dictionary():
    a = {}
    k = 0
    while (k < length):
        key = k
        value = PrimeFactors_list[k]
        a[key] = value
        k = k+1

    return a


def retrieve(listvalues_list):

    lengthl = len(listvalues_list)
    tentative_list = []
    ror = 0
    value = 0
    while (ror < lengthl):
        value = listvalues_list[ror]
        tentative_list.append(prime_dictionary[value])
        ror += 1
    return tentative_list


def add_to_multlist(some_list):

    zv = retrieve(some_list)
    varue = math.prod(zv)
    list_of_lists.append(varue)


def check_if_can_move_forward(somesuch_list):
    rength = len(somesuch_list)
    i = rength
    u = 1
    if (i > 1):
        while (u < i):
            if (somesuch_list[i-u-1]+1 != somesuch_list[i-u]):
                return i-u-1
            u = u+1
    return -1


def for_length_get_combinations(n):
    initial_positioner = 0
    left_most_index = 0
    temp_list = []
    while (initial_positioner < n):
        temp_list.append(initial_positioner)
        initial_positioner += 1
    while (True):
        add_to_multlist(temp_list)
        temp_list[-1] += 1
        if (temp_list[-1] == length):
            temp_list[-1] -= 1
            left_most_index = check_if_can_move_forward(temp_list)
            if (left_most_index == -1):
                return

            temp_list[left_most_index] += 1

            storage_left_index = 0
            uzn = 0
            storage_left_index = temp_list[left_most_index]

            left_most_index = left_most_index+1
            while (left_most_index < n):
                uzn = uzn+1
                temp_list[left_most_index] = storage_left_index + uzn
                left_most_index = left_most_index+1


def length_one_at_a_time():
    n = 1
    while (n < length):
        for_length_get_combinations(n)
        n = n+1
    return


def factorizer():
    length_one_at_a_time()
    list_of_lists.append(1)


def prime_factors_of(z):
    return_list = []
    p = 2
    o = 2
    while (z > 1):
        while (z % p == 0):
            z = z/p
            return_list.append(p)
            p = 2
            o = 2
        if (p == 2):
            p = p+1
            o = 0
        while (sympy.isprime(p+o) != True):
            o = o+2
        p = p+o
        o = 2
    return (return_list)


list_of_lists = []
u = 5
x = 3
while (x < 10000000000000000000000000):
    PrimeFactors_list = prime_factors_of(x)
    length = len(PrimeFactors_list)
    prime_dictionary = prime_factors_dictionary()
    factorizer()
    list_of_lists = list(set(list_of_lists))
    summ = sum(list_of_lists)

    print("For:", x, "T-Factors:", summ,
          "Away Perfect:", (summ-x), "% Off", (summ/x))
    if (summ-x == 0):
        "Perfect!!!!!!!!!!!!!!!!!!!!"

    list_of_lists.clear()
    PrimeFactors_list.clear()
    x = x*u

    o = 2
    while (sympy.isprime(u+o) != True):
        o = o+2
    u = u+o
