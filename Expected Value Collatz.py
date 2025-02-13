x = 1/4
n = 10000
decrease = 1/4
tracker = 0


while ((1/x) < n):
    decrease = decrease + (x * (1 - 3*x))
    x = x/2
    tracker = tracker+1

averagedecrease = decrease/tracker

averagechange = (decrease+3/2)/tracker


print("Expected Change:", averagechange)
