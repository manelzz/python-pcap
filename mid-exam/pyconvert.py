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
    fahrenheit = (temp*(9/5))+32
    return fahrenheit

def bmi(weight: float,height: float) -> str:
    '''
    BMI = weight (kg) / [height (m)]2
    '''
    bmi = weight / (height/100)**2

    if bmi < 18.5:
        status = "Underweight"
    elif bmi > 18.5 and bmi < 24.9:
        status = "Normal weight"
    elif bmi > 25.0 and bmi < 29.9:
        status = "Overweight"
    elif bmi > 30.0 and bmi < 34.9:
        status = "Obesity class I"
    elif bmi > 35.0 and bmi < 39.9:
        status = "Obesity class II"
    elif bmi > 40:
        status = "Obesity class III"
    
    return f"BMI: {bmi}, status: {status}"

def km_to_inches(distance: float) -> float:
    '''Converteix distancia de km a inches'''
    inches = distance * INCHES
    return inches

def km_to_feets(distance: float) -> float:
    '''Converteix distancia de km a feets'''
    feet = distance * FEET
    return feet

def km_to_yards(distance: float) -> float:
    yards = distance * YARDS
    '''Converteix distancia de km a yards'''    
    return yards