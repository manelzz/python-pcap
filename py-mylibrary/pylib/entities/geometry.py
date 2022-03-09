'''
Geometry Module
'''

import random
from pylib.utils import mathutils
class Color:
    
    #ATRIBUTOS O CAMPOS A NIVEL DE CLASE (STATIC/SHARED)
    MAX_VALUE: int = 255
    MIN_VALUE: int = 0
    _counter: int = 0

    #INICIALIZADOR DE OBJETO (CONSTRUCTOR)
    def __init__(self, name: str, red: int, green: int, blue: int):
        #Inicializamos el estado del objeto
        Color._counter += 1
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue

    #COMPORTAMIENTO: METODOS/OPERACIONES A NIVEL DE OBJETO O INSTANCIA
    def to_hex(self, upper:bool = True) -> str:
        '''DocString'''
        return f"#{self.red:02X}{self.green:02X}{self.blue:02X}" if upper else f"#{self.red:02x}{self.green:02x}{self.blue:02x}"

    def to_rgb(self) -> str:
        '''DocString'''
        return f"RGB({self.red},{self.green},{self.blue})"
    

    #METODOS/OPERACIONES A NIVEL DE CLASE

    @classmethod
    def random(cls) -> 'Color':
        '''DocString'''
        return cls(name = "Random Color", red = random.randint(cls.MIN_VALUE, cls.MAX_VALUE), green = random.randint(cls.MIN_VALUE, cls.MAX_VALUE), blue = random.randint(cls.MIN_VALUE, cls.MAX_VALUE))

    @classmethod
    def from_hex(cls, text: str) -> 'Color':
        '''DocString'''
        return cls(name = "Color {text}", red = int(text[1:3], base = mathutils.BASE_HEX), green = int(text[3:5],mathutils.BASE_HEX), blue = int(text[5:7], base = mathutils.BASE_HEX))

    @classmethod
    def count(cls, text: str) -> 'Color':
        '''DocString'''
        return cls._counter