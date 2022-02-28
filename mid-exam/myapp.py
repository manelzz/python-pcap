'''
Mid-exam
'''

import pyconvert

def main():
    temp_celsius = float(input(f"Introdueix temperatura Celsius: "))
    temp_fahrenheit = float(input(f"Introdueix temperatura Fahrenheit: "))
    print(f"Convesió de temperatura: {temp_fahrenheit} son {pyconvert.temp_to_celsius(temp_fahrenheit)} C")
    print(f"Convesió de temperatura: {temp_celsius} son {pyconvert.temp_to_fahrentheit(temp_celsius)} F")

    distance = float(input(f"Introdueix distancia en Km: "))
    print(f"La distancia de {distance} km en Inches és: {pyconvert.km_to_inches(distance):.2f} in")
    print(f"La distancia de {distance} km en Feets és: {pyconvert.km_to_feets(distance):.2f} ft")
    print(f"La distancia de {distance} km en Yards és: {pyconvert.km_to_yards(distance):.2f} yard")

    weight = float(input(f"Introdueix el teu pes en Kg: "))
    height = float(input(f"Introdueix la teva alçada en metres: "))
    print(f"El teu valor BMI és: {pyconvert.bmi(weight, height)}")

if __name__ == "__main__":
    main()


