qq = 0
qz = 0
q = 0
z = 18
a = 18
qqq = 0
r = 18
yn = 0
q_list = []

while (qqq < r):
    while (qq < a):
        while (q < z):
            qr = 2**q + 2**qq + 2**qqq - 1
            if (qr == 641):
                print(q, qq, qqq, "Found!")
                qqq = 18
                qq = 18
                q = 18
                yn = yn+1
                q_list.append(q)
                q_list.append(qq)
                q_list.append(qqq)
            q = q+1
            print(qr)
        qq = qq+1
        q = 0
    q = 0
    qq = 0
    qqq = qqq+1
if (yn == 0):
    print("Failed to find anything")
if (yn > 0):
    print("Found!", q_list)
