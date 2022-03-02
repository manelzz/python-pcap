'''
Main module
'''

from datetime import date
import math
from pylib.entities import geography
from pylib.entities import geometry
from pylib.utils import mathutils
from pylib.entities import planning
from pylib.utils import strutils
from pylib.utils import sysutils
from pylib.entities import staff

from pylib.entities.geography import Location
from pylib.entities.staff import Employee
from pylib.entities.geometry import Color


def main():
    '''
    Main Function
    '''

    print("*" * 100)
    print(f"Module: {mathutils.__name__}")
    print(f"PI = {mathutils.PI:.3f}")
    print(f"PHI = {mathutils.PHI:.3f}")
    print(f"E = {mathutils.E:.3f}")
    print("*" * 100)

    for i in range(5):
        print(f"{i:02d} => Even: {mathutils.is_even(i)} || Odd: {mathutils.is_odd(i)}")

    print("*" * 100)
    print(f"Module: {geography.__name__}")
    print(f"Earth Radius: {geography.EARTH_RADIUS:.2f} Kms")
    print("*" * 100)

    print("*" * 100)
    print(f"Module: {strutils.__name__}")
    print(f"DEGREES = {strutils.DEGREES}")
    print(f"DEGREES_CELSIUS = {strutils.DEGREES_CELSIUS}")
    print(f"DEGREES_FAHRENHEIT = {strutils.DEGREES_FAHRENHEIT}")
    print(f"PRIME = {strutils.PRIME}")
    print("*" * 100)
    print(f"Current year: {planning.current_year()}")
    print(f"Remaining days: {planning.remaining_days()}")
    print(f"Elapsed days: {planning.elapsed_days()}")
    print(f"IS LEAP YEAR = {planning.is_leap_year()}")
    print(f"TOTAL DAYS = {planning.total_days()}")
    print(f"PREV LEAP YEAR = {planning.prev_leap_year()}")
    print(f"NEXT LEAP YEAR = {planning.next_leap_year()}")
    print(f"YEAR PROGRESS OF 2020 = {planning.year_progress(pretty=False,year=2020)}")
    print(f"YEAR PROGRESS WITHOUT PRETTY MODE = {planning.year_progress(pretty=False)}")
    print(f"YEAR PROGRESS WITH PRETTY MODE = {planning.year_progress(2020)}")

    # for year_test in range(2010, planning.current_year()):
    #     print(f"Is year {year_test} a leap year? {planning.is_leap_year(year_test)}")

    # for year_test in range(2010, planning.current_year()):
    #     print(f"The previous leap year of year {year_test} is {planning.prev_leap_year(year_test)}.")

    # for year_test in range(2010, planning.current_year()):
    #     print(f"The next leap year of year {year_test} is {planning.next_leap_year(year_test)}.")

    print(strutils.truncate("Hola que tal estas, a ver si truncas", max_length=40))
    print(strutils.truncate("Hola que tal estas, a ver si truncas", max_length=20))
    print(strutils.truncate("Hola que tal estas, a ver si truncas", max_length=20, placeholder = "[...]"))

    for i in range(10):
        print(f"Code: {strutils.randcode()}")
        print(f"Code: {strutils.randcode(length = 12)}")
        print(f"Code: {strutils.randcode(length = 12, uppercase_letters=True, lowercase_letters=True, digits=False)}")
        print("*"*100)
        my_codes = strutils.randcodes(num_codes=100, length=12)
        print(f"Code: {len(my_codes)}")
        print(my_codes)

    print("*" *100)
    print("*" *100)

    print(F"Default Salary: {Employee.DEFAULT_SALARY}")
    print(F"Default payments: {Employee.DEFAULT_PAYMENTS}")
    e1 = Employee(firstname="Jordi", lastname="Ariño", birthdate=date(year=1995, month=2, day=1), height= 1.80, weight=65)
    e2 = Employee(firstname="Ramón", lastname="Carles", birthdate=date(year=1995, month=2, day=1), height= 1.70, weight=80)
    e3 = Employee(firstname="Elisabet", lastname="Castro", birthdate=date(year=1995, month=2, day=1), height= 1.70, weight=70)
    e4 = Employee(firstname="Enrique", lastname="Ramirez", birthdate=date(year=1995, month=2, day=1), height= 1.75, weight=73)
    e5 = Employee(firstname="Jordi", lastname="Alejandro", birthdate=date(year=1995, month=2, day=1), height= 1.85, weight=60)
    employees =[e1,e2,e3,e4,e5]
    for employee in employees:
        print(F"-"*100)
        print(F"Code: {employee.code}")
        print(F"Firstname: {employee.firstname}")
        print(F"Lastname: {employee.lastname}")
        print(F"Birthdate: {employee.birthdate}")
        print(F"Month Salary: {employee.month_salary}")
        print(F"Payments: {employee.payments}")
        print(F"Fullname: {employee.fullname()}")
        print(F"Reverse Name: {employee.reverse_name()}")
        print(F"Age: {employee.age()}")
        print(F"BMI: {employee.bmi()}")
        print(F"-"*100)
    print(F"Counter: {Employee._counter}")


    print(F"Latitude: ({Location.MIN_LATITUDE:+},{Location.MAX_LATITUDE:+})")
    print(F"Longitude: ({Location.MIN_LONGITUDE:+},{Location.MAX_LONGITUDE:+}))")
    l1 = Location(latitude=0.0, longitude=0.0)
    l2 = Location(latitude=0.0, longitude=0.0)
    l3 = Location(latitude=0.0, longitude=0.0)
    l4 = Location(latitude=0.0, longitude=0.0)
    l5 = Location(latitude=0.0, longitude=0.0)
    locations = [l1,l2,l3,l4,l5]
    print(F"Counter: {Location._counter}")

    print(F"RGB Limits: ({Color.MIN_VALUE},{Color.MAX_VALUE})")
    c1 = Color(name="Black", red=0, green=0, blue=0)
    c2 = Color(name="White", red=255, green=255, blue=255)
    c3 = Color(name="Black", red=0, green=0, blue=0)
    c4 = Color(name="Black", red=0, green=0, blue=0)
    c5 = Color(name="White", red=255, green=255, blue=255)
    colors = [c1,c2,c3,c4,c5]
    print(F"Counter: {Color._counter}")


if __name__ == "__main__":
    main()
    