import math

x = 1
q = 1
u = 1
t = 0
zn = 0

qr = 0


while (u < 1000000000000):
    while (x != 1):
        q = x
        x = x*3
        x = x+1
        while (x % 2 == 0):
            x = x/2
            zn = zn+1
        if (zn == 1):
            t = t+1
        if (zn > 1):
            t = 0
        if (t > 4):
            print("Found a ", t, " in a row increase: ", x)
        zn = 0
    x = u
    if (x < q):
        print(x, "goes through", q, "which took", t, "steps")

    u = u+2
    while (u % 3 == 0):
        u = u+2
    x = u
    t = 0
