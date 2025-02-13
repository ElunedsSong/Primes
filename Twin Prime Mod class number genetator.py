import sympy
x = 5
y = 0
z = 1000000

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


def for_primes_to_x_over_6(n):
    p = 5
    total = -1
    count = 0

    while (p < n/6):
        count = count+1
        o = 2
        if (sympy.isprime(p+o) == True):
            total = total+1
        tempp = p

        while (sympy.isprime(p+o) != True):
            o = o+2
        p = p+o

        if (check_range(list_list, tempp+1, p+(p+1)//6) == True):
            print("For", tempp, "to", p, "Claim is true", "because ",
                  check_range_return(list_list, tempp+1, p+(p+1)//6), "exists")

        if (check_range(list_list, tempp+1, p+(p+1)//6) == False):
            print("For", tempp, "to", p, "the claim is FALSE",
                  "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        if (count % 1000 == 0):
            print("Count is at", count)

    return total


for_primes_to_x_over_6(z)
