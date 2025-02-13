import sympy


x = 524119
z = 10000000


def list_make(z):
    r = 1
    second_list = []
    x = 1
    while (x < z+1):
        if x % 5 == 1 and r == 1:
            second_list.append(x)
            r = 0
        if x % 5 == 4 and r == 1:
            second_list.append(x)
            r = 0
        if x % 7 == 1 and r == 1:
            r = 0
            second_list.append(x)
        if x % 7 == 6 and r == 1:
            r = 0
            second_list.append(x)
        if x % 11 == 2 and r == 1:
            r = 0
            second_list.append(x)
        if x % 11 == 9 and r == 1:
            r = 0
            second_list.append(x)
        if x % 13 == 2 and r == 1:
            r = 0
            second_list.append(x)
        if x % 13 == 11 and r == 1:
            r = 0
            second_list.append(x)
        if x % 17 == 3 and r == 1:
            r = 0
            second_list.append(x)
        if x % 17 == 14 and r == 1:
            r = 0
            second_list.append(x)
        if x % 19 == 3 and r == 1:
            r = 0
            second_list.append(x)
        if x % 19 == 16 and r == 1:
            r = 0
            second_list.append(x)
        x = x+1
        r = 1
    if ((z-len(second_list)+3) > (z*3/5*5/7*9/11*11/13*15/17*17/19-3*6)):
        return True
    if ((z-len(second_list)+3) < (z*3/5*5/7*9/11*11/13*15/17*17/19-3*6)):
        return False


while (x < z+1):
    if (list_make(x) == False):
        print("Exception!!!!!!! : ", x)
    if (x % 1000 == 0):
        print("Just an update:", x)
    x = x+1
