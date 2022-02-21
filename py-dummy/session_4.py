'''
Main module: Dummy Code for testing
'''

import math, string
import random as rnd
import datetime as dt
import time
import os
import platform
from random import randint
from math import pi, e, sqrt
from datetime import *

print(math.pi)
print(math.sqrt(6))

print(rnd.randint(1,10))
print(rnd.randrange(1,10,2))
print(rnd.choice("AEIOU"))

fecha = dt.datetime(2023,10,23)

gen1 = rnd.Random()
gen2 = rnd.Random(100)

i = 0
while i < 20:
    print(gen1.randint(1,10))
    print(gen1.random())
    print(gen2.randint(1,10))
    print(gen2.random())
    i += 1