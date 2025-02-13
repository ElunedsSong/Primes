import sympy


list_list = []
second_list = []


x = 1
z = 524119


while (x < z+1):
    list_list.append(x)
    x = x+1

x = 1

for int in list_list:
    if int % 5 == 1:
        second_list.append(int)
    if int % 5 == 4:
        second_list.append(int)
    if int % 7 == 1:
        second_list.append(int)
    if int % 7 == 6:
        second_list.append(int)
    if int % 11 == 2:
        second_list.append(int)
    if int % 11 == 9:
        second_list.append(int)
    if int % 13 == 2:
        second_list.append(int)
    if int % 13 == 11:
        second_list.append(int)
    if int % 17 == 3:
        second_list.append(int)
    if int % 17 == 14:
        second_list.append(int)
    if int % 19 == 3:
        second_list.append(int)
    if int % 19 == 16:
        second_list.append(int)


print(len(list_list))

second_list = set(second_list)

print(len(list_list) - len(second_list)+3)


print(z*3/5*5/7*9/11*11/13*15/17*17/19-2*6)
