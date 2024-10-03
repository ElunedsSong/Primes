import math

import sympy

import numpy

r=2
v=3
k=0
i=1
z=0
u=0
j=0
fo=0
kz=0
total=0

holder_list = []

list_of_lists = []

t_tuple = ()

lengthhold=0

PrimeFactors_tuple = (2,3,5,7,11)

PrimeFactors_list = list(PrimeFactors_tuple)

length=len(PrimeFactors_tuple)

print(PrimeFactors_tuple)


def primefactorsdictionary():
    a = {} 
    k = 0 
    while k < length: 
        # dynamically create key 
        key = k 
        # calculate value 
        value = PrimeFactors_list[k] 
        a[key] = value  
        k = k +1
    
    return(a)

a=primefactorsdictionary()


def retrieve(listvalues_list):

    lengthl=len(listvalues_list)
    tentative_list = []
    ror=0
    value=0
    while(ror<lengthl):
        value=listvalues_list[ror]
        tentative_list.append(a[value])
        ror+=1

    return (tentative_list)

def addtomultlist(some_list):

    zv = retrieve(some_list)
    varue= math.prod(zv)
    list_of_lists.append(varue)


def checkifcanmoveforward(somesuch_list):

    rength=len(somesuch_list)
    i=rength    
    u=1
    if(i>1):
        while(u<i):
            if(somesuch_list[i-u-1]+1!=somesuch_list[i-u]):
                return (i-u-1)
            u=u+1
    return -1 

def listclearcopy(somerlist,somerestlist):

    somerlist.clear()
    somerlist = somerestlist

    return



def fun3(n):
    urntracker=1
    tracker=0
    pigsdontfly=0
    rv=0
    urn=0
    original_list=[]
    temp_list = []
    urn_list = []
    while (rv<n):
        temp_list.append(rv)
        rv+=1
    original_list = temp_list[:]
    print(original_list)
    while(pigsdontfly<10):
        print(temp_list)
        addtomultlist(temp_list)
        temp_list[-1] +=1
        if (temp_list[-1]==length):
            temp_list[-1] -=1
            urn = checkifcanmoveforward(temp_list)
            if (urn==-1):
                return
            
            temp_list[urn] +=1

            storageurn=0
            uzn=0
            storageurn = temp_list[urn]

            print(urn)

            urn=urn+1
            while (urn<n):
                uzn=uzn+1
                temp_list[urn] = storageurn + uzn
                urn=urn+1

        pigsdontfly=pigsdontfly+1


def fun():
    n=1
    while(n<length):
        fun3(n)
        n=n+1
    n=1
    return

def factorizer():
    fun()
    list_of_lists.append(1)

factorizer()



print(list_of_lists)

factordone_list = list(set(list_of_lists))


factordone_list.sort()

print(factordone_list)

total = sum(factordone_list)

print(total)


        