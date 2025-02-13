y = .2
z = .8
v = 0
total = 0

while (v < 10000000):
    total = total + (y * (z**v)*v)
    v = v+1
print(total)
