'''
Format data to print
'''

from cgi import print_directory
import math
import random
from sys import path_hooks
from turtle import st


op1 = random.randint(1,100)
op2 = random.randint(1,100)
op3 = random.randint(1,100)
rmax =max(op1, op2)
rmin =min(op1, op2)
rqsrt = math.sqrt(op3)

print('MAX({},{}) ={}'.format(op1, op2, rmax))
print('MAX({0},{1}) ={2} \nMIN({0},{1}) = {3}\n'.format(op1, op2, rmax, rmin))
print('MAX({p1},{p2}) ={p3} \nMIN({p1},{p2}) = {p4}\n'.format(p1= op1, p2 = op2, 
                                                                p3= rmax, p4 = rmin))

print('SQRT({p1}) = {result:.2f}'.format(p1 = op3, result = rqsrt))
print('Decimal: {0:d} Hexadecimal: {0:X} Octal: {0:o}'.format(255))


print('Porcentaje: {p1}, {p2} = {p3:%}'.format(p1 = 1, p2 = 2, p3= 1/2))

rpath1 = r'C:\Windows\system32\cmd.exe'
print(rpath1)

v1 = input("Enter a value: ")
i1 = int(input("Enter a number: "))