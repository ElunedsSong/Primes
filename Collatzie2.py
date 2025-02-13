import math

n = 50000000000000000000000000
qn = 0
vz = 0


while (n < 100000000000000000000000000):
    u = n
    while (u % 3 == 0):
        u = u//3
    while (qn < 3):
        u = 3*u + 1
        while (u % 2 == 0):
            u = u//2
        qn = qn+1
    if (u > n):
        print("Error Value at:", n)
    if (u < n):
        if (vz > 1000000):
            vz = 0
            print("Success Value at!!!!!!!!", n)
    vz = vz+1
    qn = 0
    n = n+2
