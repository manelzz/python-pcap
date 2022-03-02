'''
Geometry Module
'''

class Color:
    
    #ATRIBUTOS O CAMPOS A NIVEL DE CLASE (STATIC/SHARED)
    MAX_VALUE: int =255
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
