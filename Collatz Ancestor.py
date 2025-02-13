import math

x = 5
z = 1

list_of_connected_ancestors = []

list_temp = []
list_temp2 = []


def GenerateDirectAncestralLine(x):
    z = 1
    while (x < 3200):
        while (z == 1):
            x = x*2
            if (x % 18 == 4):
                z = 0
            if (x % 18 == 16):
                z = 0
        x = x-1
        x = x/3
        if (x < 100):
            list_of_connected_ancestors.append(x)
        list_temp.append(x)
        list_of_connected_ancestors.append(x)
        z = 1


def GenerateInDirectAncestralLine(x):
    z = 1
    while (x < 3200):
        while (z == 1):
            x = x*2
            if (x % 18 == 4):
                z = 0
            if (x % 18 == 16):
                z = 0
        x = x-1
        x = x/3
        if (x < 100):
            list_of_connected_ancestors.append(x)
        list_temp2.append(x)
        list_of_connected_ancestors.append(x)
        x = x*3
        x = x+1
        z = 1


while (True):
    GenerateInDirectAncestralLine(5)
    a = list(set(list_temp2))
    a.sort()
    q = len(a)
    u = 0
    while (u < q):
        v = a[u]
        GenerateDirectAncestralLine(v)
        u = u+1
    list_temp2.clear
    a.clear()


ancestors = list(set(list_of_connected_ancestors))
ancestors.sort()

print(ancestors)


x = 1

while (x < 100):
    if (x % 3 != 0):
        print(x)
    x = x+2
