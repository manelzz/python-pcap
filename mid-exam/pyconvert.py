'''
Functions class
'''

INCHES: float = 39370.07874
FEET: float = 3280.839895
YARDS: float = 1093.6132298

#CLASS LEVEL FUNCTIONS
def temp_to_celsius(temp: float) -> float:
    ''' Conveteix temperatura de Fahrenheit a Celsius'''
    celsius = (temp-32)*(5/9)
    return celsius

def temp_to_fahrentheit(temp: float) -> float:
    ''' Conveteix temperatura Celsius a Fahrenheit'''
    fahrenheit = (temp*(5/9))+32
    return fahrenheit

def bmi(weight: float,height: float) -> str:
    '''
    BMI = weight (kg) / [height (m)]2
    '''
    bmi = weight / (height*height)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi in range(18.5,24.9):
        status = "Normal weight"
    elif bmi in range(25.0,29.9):
        status = "Overweight"
    elif bmi in range(30.0,34.9):
        status = "Obesity class I"
    elif bmi in range(35.0,39.9):
        status = "Obesity class II"
    elif bmi > 40:
        status = "Obesity class III"
    
    return f"BMI: {bmi}, status: {status}"

def km_to_inches(distance: float) -> float:
    '''Converteix distancia de km a inches'''
    inches = (distance * INCHES) / 100
    return inches

def km_to_feets(distance: float) -> float:
    '''Converteix distancia de km a feets'''
    feet = (distance * FEET) / 100
    return feet

def km_to_yards(distance: float) -> float:
    yards = (distance * YARDS) / 100
    '''Converteix distancia de km a yards'''    
    return yards