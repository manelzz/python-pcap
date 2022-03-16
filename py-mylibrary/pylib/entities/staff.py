'''
Staff Module
'''

from code import interact
from datetime import date, datetime

from pylib.utils import strutils
import math


class Employee:

    #ATRIBUTOS O CAMPOS A NIVEL DE CLASE (STATIc/SHARED)
    DEFAULT_SALARY: float = 1200.0
    DEFAULT_PAYMENTS: int  = 12
    _counter: int = 0

    #INICIALIZADOR DE OBJETO (CONSTRUCTOR)
    def __init__(self, firstname: str, lastname: str, birthdate: date, height: float, weight: float, monthly_salary:float = DEFAULT_SALARY, payments: int = DEFAULT_PAYMENTS, hiredate: date = date.today()):
        # ----> []object > Inicializar el estado de este objeto
        #Inicializamos los atributos o campos de instanacia a objeto (self.XXX)
        Employee._counter +=1
        self.code = f"E{Employee._counter:03d}"
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.height = height
        self.weight = weight
        self.monthly_salary = monthly_salary
        self.payments = payments
        self.hiredate = hiredate

    #COMPORTAMIENTO: METODOS/OPERACIONES A NIVEL DE OBJETO O INSTANCIA
    def fullname(self) -> str:
        '''DocString'''
        return f"{self.firstname} {self.lastname}"

    def reverse_name(self) -> str:
        '''DocString'''
        return f"{self.lastname} {self.firstname}"

    def annual_salary(self) -> float:
        '''Phyton DocString'''
        return self.DEFAULT_PAYMENTS * self.DEFAULT_PAYMENTS
        
    def age(self) -> int:
        '''DocString'''
        interval = date.today() - self.birthdate
        return math.floor(interval.days/365)

    def seniority(self)-> int:
        '''Calcula dies d'antiguitat a l'empresa'''
        interval = date.today() - self.hiredate
        return interval

    def bmi(self) -> tuple[float,str]:
        '''DocString'''
        category= strutils.EMPTY
        bmi = self.weight / math.pow(self.height,2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi > 18.5 and bmi < 25.0:
            category = "Normal weight"
        elif bmi > 25.0 and bmi < 30.0:
            category = "Overweight"
        elif bmi > 30.0 and bmi < 35.0:
            category = "Obesity class I"
        elif bmi > 35.0 and bmi < 40.0:
            category = "Obesity class II"
        elif bmi > 40:
            category = "Obesity class III"

        return (bmi,category)

    def __str__(self) -> str:
        """Python DocString"""
        return f"{self.code} > {self.fullname()}: {self.monthly_salary}"

    def __len__(self) -> int:
        """Python DocString"""
        return self.seniority()

    def __lt__(self, other: 'Employee') -> bool:
        """Python DocString"""
        if not isinstance(other, Employee):
            raise TypeError("You can only compare with another Employee")

        return self.age() < other.age()

    def __le__(self, other: 'Employee') -> bool:
        """Python DocString"""
        if not isinstance(other, Employee):
            raise TypeError("You can only compare with another Employee")

        return self.age() <= other.age()

    def __gt__(self, other: 'Employee') -> bool:
        """Python DocString"""
        if not isinstance(other, Employee):
            raise TypeError("You can only compare with another Employee")

        return self.age() > other.age()

    def __ge__(self, other: 'Employee') -> bool:
        """Python DocString"""
        if not isinstance(other, Employee):
            raise TypeError("You can only compare with another Employee")

        return self.age() >= other.age()

    
    def __add__(self, value: int|float) -> 'Employee':
        """Python DocString"""
        self.monthly_salary += value
        return self

    def __sub__(self, value: int|float) -> 'Employee':
        """Python DocString"""
        self.monthly_salary -= value
        return self
    
    def __mul__(self, value: int|float) -> 'Employee':
        """Python DocString"""
        self.monthly_salary *= value
        return self

    def __truediv__(self, value: int|float) -> 'Employee':
        """Python DocString"""
        self.monthly_salary /= value
        return self

    
    def __del__(self):
        """Python DocString"""
        print("-" * 100)
        print(f"Estoy muriendome --> {str(self)}")
        print("-" * 100)