'''
Geography Module
'''

from cmath import cos
import math

from numpy import mat
from sqlalchemy import lateral
from pylib.utils import strutils


EARTH_RADIUS: int = 6370

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


    # Interpolations strings

    def latitude_deg(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        if cpoint:
            if self.latitude > 0:
                cp = "N"
            else: 
                cp = "S"
                self.latitude = self.latitude * (-1)
        
        return f"{abs(self.latitude):.{decimals}f} {strutils.DEGREES} {cp}" if cpoint else f"{self.latitude:.{decimals}f} {strutils.DEGREES}"
     


    def longitude_deg(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        if cpoint:
            if self.longitude > 0:
                cp = "E"
            else:
                self.longitude = self.longitude * (-1)
                cp = "O"
        
        return f"{abs(self.longitude):.{decimals}f} {strutils.DEGREES} {cp}" if cpoint else f"{self.longitude:.{decimals}f} {strutils.DEGREES}"

    
    def to_degrees(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        return f"Latitut: {self.latitude_deg(decimals, cpoint)} Longitut: {self.longitude_deg(decimals, cpoint)}"


    # ----------------------------------------------------

    # Interpolation string + math operations

    def latitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        degrees = int(self.latitude)
        ms = (self.latitude - int(self.latitude)) * 60
        minutes = int(ms)
        seconds = (ms - int(ms)) * 60

        if cpoint:
            if self.longitude > 0:
                cp = "N"
            else:
                self.longitude = self.longitude * (-1)
                cp = "S"

        return f"{abs(degrees)}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds}{strutils.DOUBLE_PRIME} {cp}" if cpoint else f"{degrees}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds}{strutils.DOUBLE_PRIME}"


    def longitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        degrees = int(self.longitude)
        ms = (self.longitude - int(self.longitude)) * 60
        minutes = int(ms)
        seconds = (ms - int(ms)) * 60

        if cpoint:
            if self.longitude > 0:
                cp = "E"
            else:
                self.longitude = self.longitude * (-1)
                cp = "O"

        return f"{abs(degrees)}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds}{strutils.DOUBLE_PRIME} {cp}" if cpoint else f"{degrees}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds}{strutils.DOUBLE_PRIME}"

    def to_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        return f"Latitut: {self.latitude_dms(decimals, cpoint)} Longitude: {self.longitude_dms(decimals, cpoint)}"
    
    # ----------------------------------------------------
    
    # Match operations

    def distance_to(self, other: 'Location') -> float:
        '''
        Python DocString
        '''
        rlat1 = math.radians(self.latitude)
        rlong1 = math.radians(self.longitude)

        rlat2 = math.radians(other.latitude)
        rlong2 = math.radians(other.longitude)

        dlat = rlat2 - rlat1
        dlong =  rlong2 - rlong1

        a = math.pow(math.sin((dlat)/2),2) + math.cos(rlat1) * \
            math.cos(rlat2) * math.pow(math.sin((dlong)/2),2)
        c= 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
        return EARTH_RADIUS * c
        
        raise NotImplementedError("Not yet implemented!")

    def midpoint_to(self, other: 'Location') -> 'Location':
        '''
        Python DocString
        '''

        rlat1 = math.radians(self.latitude)
        rlong1 = math.radians(self.longitude)

        rlat2 = math.radians(other.latitude)
        rlong2 = math.radians(other.longitude)

        dlat = rlat2 - rlat1
        dlong =  rlong2 - rlong1

        bx = math.cos(rlat2) * math.cos(dlong)
        by = math.cos(rlat2) * math.sin(dlong)

        lat = math.degrees(math.atan2(math.sin(rlat1) + math.sin(rlat2), math.sqrt((math.cos(rlat1) + bx) ** 2 + by ** 2)))
        long = math.degrees(rlong1 + math.atan2(by, math.cos(rlat1) + bx))
        name = print(f"{self.name}-{other.name}")
        
        return Location (name, lat, long)