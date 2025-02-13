import sympy
x = 5
y = 0
z = 20000

list_list = []


def check_range(lst, lower, upper):
    for num in lst:
        if lower <= num <= upper:
            return True
        if (num > upper):
            return False
    return False


def check_range_return(lst, lower, upper):
    for num in lst:
        if lower <= num <= upper:
            return num
        if (num > upper):
            return False
    return False


def twin_primes_to_x(n):
    p = 3
    total = 0

    while (p < n):
        o = 2
        if (sympy.isprime(p+o) == True):
            list_list.append((p+o-1)//6)
        while (sympy.isprime(p+o) != True):
            o = o+2

        p = p+o

    return list_list


twin_primes_to_x(z)
list_list.pop(0)

print(list_list)


def check_list_range(lower, upper, list_of_lists):
    count = 0
    for num in list_of_lists:
        if lower < num < upper:
            count = count+1
        if num >= upper:
            return count
    return count


def twin_primes_to_x2(n):
    p = 5
    ratio = 1
    total = 0
    compareratio = 0
    while (p < n):
        oldp = p
        o = 2
        ratio = ratio*((p-2)/p)
        while (sympy.isprime(p+o) != True):
            o = o+2

        p = p+o
        compareratio = compareratio+check_list_range(
            oldp-(oldp+1)//6, p-(p+1)//6, list_list)
        total = total + p-(p+1)//6 - (oldp-(oldp+1)//6) - 1
        print("Ratio for", oldp, "to", p, "is",
              ratio, "comapred to", compareratio/total)
    return


twin_primes_to_x2(z/6)
