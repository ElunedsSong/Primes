import math


n = 0
qz = 0
qr = 0

t = 0

while (n < 1000):

    u = 5 * (3 ** n)

    while (u != 4):
        qr = u
        while (u % 2 == 0):
            u = u/2
        if (u == 1):
            if ((math.log2(qr)) % 2 == 0):
                qz = qz+1
                print("For:", n, "Correct!",
                      "Total Correct Count:", qz, "How Many:", qz-(n+1))
        u = 3*u + 1
    t = 0
    n = n+1
