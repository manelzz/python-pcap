'''
Geometry Module
'''

from abc import ABC
import random
from pylib.utils import mathutils
class Color(object):
    
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

    

    @property
    def name(self) -> str:
        """Python DocString"""
        return self._name

    @name.setter
    def name(self, value: str) :
        """Python DocString"""
        if not type(value) is str:
            raise TypeError("Name must be of type str")

        self._name = value


    @property
    def red(self) -> int:
        """Python DocString"""
        return self._red

    @red.setter
    def red(self, value: int):
        """Python DocString"""
        if not type(value) is int:
            raise TypeError("Red must be of type int")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE:
            raise ValueError("Red coordinate is out of range")
        
        self._red = value
    
    @property
    def green(self) -> int:
        """Python DocString"""
        return self._green
    
    @green.setter
    def green(self, value: int):
        """Python DocString"""
        if not type(value) is int:
            raise TypeError("Green must be of type int")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE:
            raise ValueError("Green coordinate is out of range")
        
        self._green = value
    
    @property
    def blue(self) -> int:
        """Python DocString"""
        return self._blue

    @blue.setter
    def blue(self, value: int):
        """Python DocString"""
        if not type(value) is int:
            raise TypeError("Blue must be of type int")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE:
            raise ValueError("Blue coordinate is out of range")
        
        self._blue = value


    def __str__(self) -> str:
        '''Python DocString'''
        return f"{self.name} {self.to_hex()}"
   
    def __eq__(self, other: 'Color') -> bool:
        """Python DocString"""
        if not isinstance(other, Color):
            raise TypeError(f"The value to compare must be of type Color")
        
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __ne__(self, other: 'Color') -> bool:
        """Python DocString"""
        if not isinstance(other, Color):
            raise TypeError(f"The value to compare must be of type Color")
        
        return not self.__ne__(other)



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
    def count(cls) -> int:
        '''Python DocString'''
        return cls._counter


class AlphaColor(Color):

    MAX_ALPHA: int = 100
    MIN_ALPHA: int = 0

    def __init__(self, name: str, red: int, green: int, blue: int, alpha: int):
        super().__init__(name, red, green, blue)
        self._alpha =alpha

    @property
    def alpha(self) -> int:
        return self._alpha

    @alpha.setter
    def alpha(self, value: int):
        if not isinstance(value, float):
            raise TypeError("Valor Alpha no es float")
        self._alpha = value

    def to_rgb(self) -> str:
        return f"{super().to_rgb()} - A: {self.alpha}%"

    def to_hex(self, upper: bool = True) -> str:
        return f"{super().to_hex(upper)} - A: {self.alpha}%"

from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self, background_color: 'Color', fore_color: 'Color') -> None:
        self.background_color = background_color
        self.fore_color = fore_color
    
    #obligamos a nuestros tipos hijos a implementar estos metodos
    @abstractmethod
    def area(self)-> float:
        return

    @abstractmethod
    def perimeter(self)-> float:
        return


class Square(Shape):
    def __init__(self, side: float|int, background_color: 'Color' = Color.from_hex("#CCCCCC"), fore_color: 'Color' = Color.from_hex("#00000")) -> None:
        super().__init__(background_color, fore_color)
        self._side = side
    
    @property
    def side(self) -> float|int:
        return self._side

    def area(self) -> float:
        return self.side ** 2
    
    def perimeter(self) -> float:
        return self.side * 4

class Rectangle(Shape):
    pass

class Triangle(Shape):
    pass
