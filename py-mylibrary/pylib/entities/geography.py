'''
Geography Module
'''

EARTH_RADIUS: int = 6370

class Location:

    #ATRIBUTOS O CAMPOS A NIVEL DE CALSE (STATIC/SHARED)
    MAX_LATITUDE:float = 90.0
    MIN_LATITUDE:float = -MAX_LATITUDE
    MAX_LONGITUDE:float = 180.0
    MIN_LONGITUDE:float = -MAX_LONGITUDE
    _counter: int = 0

    #INICIALIZADOR DE OBJETO (CONSTRUCTOR)
    def __init__(self, latitude:float, longitude: float):
        # --> [](self) > Misión: Inicialitzar el estado inicial del objeto
        Location._counter += 1
        self.latitude = latitude
        self.longitude = longitude
    