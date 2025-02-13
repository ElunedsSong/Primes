import math
import sympy
import numpy

list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []
factor1 = 641
factor2 = 274177
factor3 = 59649589127497217
factor4 = 7455602825647884208337395736200454918783366342657
factor5 = 4659775785220018543264560743076778192897
factor6 = 3560841906445833920513
factor7 = 33550336
factor8 = factor2*factor7
qn = 0


while (factor1 > 0):

    z = math.floor(math.log2(factor1))
    factor1 = factor1 - 2**z
    list_1.append(z)

while (factor2 > 0):

    z = math.floor(math.log2(factor2))
    factor2 = factor2 - 2**z
    list_2.append(z)

while (factor3 > 0):

    z = math.floor(math.log2(factor3))
    factor3 = factor3 - 2**z
    list_3.append(z)

while (factor4 > 0):

    z = math.floor(math.log2(factor4))
    factor4 = factor4 - 2**z
    list_4.append(z)

while (factor5 > 0):

    z = math.floor(math.log2(factor5))
    factor5 = factor5 - 2**z
    list_5.append(z)
while (factor6 > 0):

    z = math.floor(math.log2(factor6))
    factor6 = factor6 - 2**z
    list_6.append(z)
while (factor7 > 0):

    z = math.floor(math.log2(factor7))
    factor7 = factor7 - 2**z
    list_7.append(z)
while (factor8 > 0):

    z = math.floor(math.log2(factor8))
    factor8 = factor8 - 2**z
    list_8.append(z)


print(list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8)
