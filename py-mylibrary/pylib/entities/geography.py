'''
Geography Module
'''

from cmath import cos
from lib2to3.pgen2.token import MINUS
import math
import random
from numpy import mat
from sqlalchemy import lateral
from pylib.utils import strutils
from pylib.utils import mathutils


EARTH_RADIUS: int = 6370

def degrees_to_dms(value:float) -> tuple[int,int,float]:
    degrees = int(value)
    fminutes = abs(value - degrees) * 60
    minutes = int(fminutes)
    seconds = (fminutes - int(fminutes)) * 60
    
    return (degrees, minutes, seconds)
        
class Location:

    #ATRIBUTOS O CAMPOS A NIVEL DE CALSE (STATIC/SHARED)
    MAX_LATITUDE:float = 90.0
    MIN_LATITUDE:float = -MAX_LATITUDE
    MAX_LONGITUDE:float = 180.0
    MIN_LONGITUDE:float = -MAX_LONGITUDE
    _counter: int = 0

    #INICIALIZADOR DE OBJETO (CONSTRUCTOR)
    def __init__(self, name: str, latitude:float, longitude: float):
        # --> [](self) > Misión: Inicialitzar el estado inicial del objeto
        Location._counter += 1
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    @property
    def name(self) -> str:
        '''Python Docstring'''
        return self._name

    @name.setter
    def name(self, value: str):
        '''Python Docstring'''
        if not isinstance(value, str):
            raise TypeError(f"The name must be of type str.")

        self._name = value

    @property
    def latitude(self) -> float:
        '''Python Docstring'''
        return self._latitude

    @latitude.setter
    def latitude(self, value: float):
        '''Python Docstring'''
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError(f"The latitude must be of type float or int.")
        if value < Location.MIN_LATITUDE or value > Location.MAX_LATITUDE:
            raise ValueError(f"The latitude is out of range. Range: {Location.MIN_LATITUDE}, {Location.MAX_LATITUDE}")    

        self._latitude = value

    @property
    def longitude(self) -> float:
        '''Python Docstring'''
        return self._longitude
    
    @longitude.setter
    def longitude(self, value: float):
        '''Python Docstring'''
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError(f"The longitude must be of type float or int.")
        if value < Location.MIN_LONGITUDE or value > Location.MAX_LONGITUDE:
            raise ValueError(f"The longitude is out of range. Range: {Location.MIN_LONGITUDE}, {Location.MAX_LONGITUDE}")    

        self._longitude = value
        
    
    # COMPORTAMIENTO: METODOS/OPERACIONES A NIVEL DE OBJETO O INSTANCIA
    def latitude_deg(self, decimals: int = 5, cpoint: bool = True) -> str:
        """Python DocString"""
        return f"{self.latitude:.{decimals}f}{strutils.DEGREES}" if not cpoint else f"{abs(self.latitude):.{decimals}f}{strutils.DEGREES} {'N' if self.latitude >= 0 else 'S'}"

    def longitude_deg(self, decimals: int = 5, cpoint: bool = True) -> str:
        """Python DocString"""
        return f"{self.longitude:.{decimals}f}{strutils.DEGREES}" if not cpoint else f"{abs(self.longitude):.{decimals}f}{strutils.DEGREES} {'E' if self.longitude >= 0 else 'W'}"
    
    def to_degrees(self, decimals: int = 5, cpoint: bool = True) -> str:
        """Python DocString"""
        return f"{self.latitude_deg(decimals, cpoint)} {self.longitude_deg(decimals, cpoint)}"


    def latitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        """Python DocString"""
        (degrees, minutes, seconds) = degrees_to_dms(self.latitude)
        return f"{degrees}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME}" if not cpoint else f"{abs(degrees)}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME} {'N' if degrees >= 0 else 'S'}"

    def longitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        """Python DocString"""
        (degrees, minutes, seconds) = degrees_to_dms(self.longitude)
        return f"{degrees}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME}" if not cpoint else f"{abs(degrees)}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME} {'E' if degrees >= 0 else 'W'}"

    def to_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        """Python DocString"""
        return f"{self.latitude_dms(decimals, cpoint)}  {self.longitude_dms(decimals, cpoint)}"

    def distance_to(self, other: 'Location') -> float:
        """Python DocString"""
        (rlat1, rlong1, rlat2, rlong2, dlat, dlong)  = Location._convert_radians(self, other)
        a = math.pow(math.sin(dlat/2), 2) + math.cos(rlat1) * math.cos(rlat2) * math.pow(math.sin(dlong/2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return EARTH_RADIUS * c

    def midpoint_to(self, other: 'Location') -> 'Location':
        """Python DocString"""
        (rlat1, rlong1, rlat2, rlong2, dlat, dlong)  = Location._convert_radians(self, other)
        bx = math.cos(rlat2) * math.cos(dlong)
        by = math.cos(rlat2) * math.sin(dlong)
        lat = math.degrees(math.atan2(math.sin(rlat1) + math.sin(rlat2), math.sqrt((math.cos(rlat1) + bx) ** 2 + by ** 2)))
        long = math.degrees(rlong1 + math.atan2(by, math.cos(rlat1) + bx))
        
        return Location(f"Midpoint: {self.name}-{other.name}", lat, long)


    def __str__(self) -> str:
        """Python DocString"""
        return f"{self.name} > {self.to_dms()}"
    

    def __eq__(self, other: 'Location') -> bool:
        """Python DocString"""
        if not isinstance(other, Location):
            raise TypeError(f"The value to compare must be of type Location")
        
        return self.latitude == other.latitude and self.longitude == other.longitude

    def __ne__(self, other: 'Location') -> bool:
        """Python DocString"""
        if not isinstance(other, Location):
            raise TypeError(f"The value to compare must be of type Location")
        
        return not self.__eq__(other)


    def __sub__(self, other: 'Location') -> 'Location':
        """Python DocString"""
        if not isinstance(other, Location):
            raise TypeError(f"The value to substract must be of type Location")
        
        return self.midpoint_to(other)


    # MÉTODOS/OPERACIONES A NIVEL DE CLASE 
    @classmethod
    def random(cls) -> 'Location':
        """Python DocString"""
        return cls(name = "Random Localization", latitude = random.uniform(cls.MIN_LATITUDE, cls.MAX_LATITUDE), longitude = random.uniform(cls.MIN_LONGITUDE, cls.MAX_LONGITUDE))

    @classmethod
    def count(cls) -> int:
        """Python DoctString"""
        return cls._counter

    @staticmethod
    def _convert_radians(l1: 'Location', l2: 'Location') -> tuple[float,float,float,float,float,float]:
        rlat1 = math.radians(l1.latitude)
        rlong1 = math.radians(l1.longitude)
        rlat2 = math.radians(l2.latitude)
        rlong2 = math.radians(l2.longitude)
        dlat = rlat2 - rlat1
        dlong = rlong2 - rlong1
        return (rlat1,rlong1,rlat2,rlong2,dlat,dlong)
