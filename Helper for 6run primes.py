x = 14
y = 210
z = 41
q = 0
while (q == 0):
    if (x % 210 != 0):
        x = x+z
    if (x % 210 == 0):
        q = 1
print(x, x/210)
