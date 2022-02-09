"""
first test
"""

from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import math
import os
import random

from numpy import mat


print("Hello World")
print(math.e)
print(math.pi)
print(math.sqrt(4))
print(random.randint(a=1, b=100))
print(random.randrange(start = 5, stop = 500, step = 5))

print("A","B","C",'C','D')
print("A","B","C",'C','D', sep ='*****', end = '\n\n\n')
print("A","B","C",'C','D', sep ='\n', end = '*****')
print("hola", end ="")
print()

op1 = random.randint(1,100)
#show memory address references of variable 'op1'
print(hex(id(op1)))
op2 = random.randint(1,100)
op3 = random.randint(1,100)
rmax =max(op1, op2)
rmin =min(op1, op2)
rqsrt = math.sqrt(op3)


