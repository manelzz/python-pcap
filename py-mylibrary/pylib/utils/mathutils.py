'''
Math Utils
'''

#MODULE LEVEL Global attributs or Global variables
PI =3.141592653589
E =  2.718281828459045235360
PHI = 1.618033988
BASE_HEX = 16

#CLASS LEVEL FUNCTIONS

def abs(value: int|float) -> int|float:
    '''
    Calculate absolute value of a given number
    '''
    return value if value >= 0 else -value

def is_even(value: int) -> bool:
    '''
    Return true if value is an even number
    '''
    return value%2 == 0

def is_odd(value: int) -> bool:
    '''
    Return true if value is an odd number
    '''
    return value%2 != 0