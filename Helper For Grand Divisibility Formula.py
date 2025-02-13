

b = 2
z = 9
w = 13
q = 1

n = z*q*w


answer = (b**n-1) % ((((b**(w)+1)*(b**(w)))+1))
answer_as_long_number = (b**n-1) / ((((b**(w)+1)*(b**(w)))+1))


print(answer)
print(answer_as_long_number)
