'''
Main Module
'''
from datetime import date,datetime,timedelta

from pylib.utils import strutils          #pylib.utils.strutils
from pylib.utils import mathutils         #pylib.utils.mathutils
from pylib.utils import sysutils          #pylib.utils.sysutils
from pylib.entities import planning       #pylib.entities.planning
from pylib.entities import geography      #pylib.entities.geography
from pylib.entities import geometry       #pylib.entities.geometry
from pylib.entities import staff          #pylib.entities.staff

from pylib.entities.geography import Location
from pylib.entities.staff import Employee, SalesEmployee
from pylib.entities.geometry import Color, AlphaColor, Shape, Square, Triangle, Rectangle
from pylib.entities.planning import Event


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
        print("*"*50)
        my_codes = strutils.randcodes(num_codes=100, length=12)
        print(f"Code: {len(my_codes)}")
        print(my_codes)

    print("*" *50)
    print("*" *50)

    print(F"Default Salary: {Employee.DEFAULT_SALARY}")
    print(F"Default payments: {Employee.DEFAULT_PAYMENTS}")
    e1 = Employee(firstname = "Jordi", lastname = "Ariño", birthdate = date(year = 1980, month = 10, day = 23), height = 1.86, weight = 80, hiredate = date(year = 1995, month = 5, day = 5))
    e2 = Employee(firstname = "Ramon", lastname = "Carles", birthdate = date(year = 1985, month = 11, day = 15), height = 1.76, weight = 70, hiredate = date(year = 2012, month = 5, day = 5))
    e3 = Employee(firstname="Elisabet", lastname="Castro", birthdate=date(year=1995, month=2, day=1), height= 1.70, weight=70)
    e4 = Employee(firstname="Enrique", lastname="Ramirez", birthdate=date(year=1995, month=2, day=1), height= 1.75, weight=73)
    e5 = Employee(firstname="Jordi", lastname="Alejandro", birthdate=date(year=1995, month=2, day=1), height= 1.85, weight=60)
    e6 = SalesEmployee(firstname="Vladimir", lastname="Putin", birthdate=date(year=1995, month=2, day=1), height= 1.85, weight=60, comission= 1000)
    employees =(e1,e2,e3,e4,e5,e6)
    for employee in employees:
        print(F"-"*50)
        print(F"Code: {employee.code}")
        print(F"Firstname: {employee.firstname}")
        print(F"Lastname: {employee.lastname}")
        print(F"Birthdate: {employee.birthdate}")
        print(F"Month Salary: {employee.monthly_salary}")
        print(F"Payments: {employee.payments}")
        print(F"Fullname: {employee.fullname()}")
        print(F"Reverse Name: {employee.reverse_name()}")
        print(F"Age: {employee.age()}")
        print(F"BMI: {employee.bmi()}")
        print(F"-"*50)

    print(e1 > e2)
    print(e1 >= e2)
    print(e1 < e2)
    print(e1 <= e2)
    print(e1)
    #print(len(e1))
    
    print(e1)
    e1 * 5
    print(e1)
    print(e1)
    e1 + 100
    print(e1)
    e1 - 100
    print(e1)
    
    print(F"Counter: {Employee._counter}")

    c = Square(side = 2)
    print(f"Square side 2: {c}")

    print(F"Latitude: ({Location.MIN_LATITUDE:+},{Location.MAX_LATITUDE:+})")
    print(F"Longitude: ({Location.MIN_LONGITUDE:+},{Location.MAX_LONGITUDE:+}))")
    
    mad = Location(name="Madrid", latitude = 40.4165, longitude=-3.70256)
    bcn = Location(name="Barcelona", latitude = 41.38879, longitude=2.15899)
    paris = Location(name="Paris", latitude = 48.85341, longitude=2.3488)
    ny = Location(name="New York", latitude = 40.71427, longitude=-74.00597)
    prnd1 = Location.random()

    locations = (mad, bcn, paris, ny, prnd1)
    
    print(F"Counter: {Location._counter}")
    for location in locations:
        print("-" * 50)
        print(f"Ciutat: {location.name}")
        print(f"Latitude: {location.latitude_deg(decimals = 3, cpoint=False)}")
        print(f"Longitud: {location.longitude_deg(decimals = 3, cpoint=False)}")
        print(f"Coordinades: {location.to_degrees(decimals = 4, cpoint=False)}")
        print(f"Latitude: {location.latitude_deg(decimals = 3)}")
        print(f"Longitud: {location.longitude_deg(decimals = 3)}")
        print(f"Coordinades: {location.to_degrees(decimals = 4)}")
        print("-" * 50)
        print(f"Latitude: {location.latitude_dms(decimals = 3, cpoint=False)}")
        print(f"Longitud: {location.longitude_dms(decimals = 3, cpoint=False)}")
        print(f"Coordinades: {location.to_dms(decimals = 4, cpoint=False)}")
        print(f"Latitude: {location.latitude_dms(decimals = 3)}")
        print(f"Longitud: {location.longitude_dms(decimals = 3)}")
        print(f"Coordinades: {location.to_dms(decimals = 4)}")
        print("-" * 50)
        print(f"Distancia: {location.distance_to(mad)} Km")
        print(f"Punt intermig: {location.midpoint_to(mad).to_degrees()}")

    print(f"BCN-MAD: {bcn.distance_to(mad)} Km")
    print(f"BCN-NY: {bcn.distance_to(ny)} Km")
    print(f"BCN-NY: {bcn.distance_to(paris)} Km")

    print(f"BCN-MAD: {bcn.midpoint_to(mad).to_degrees()}")
    print(f"BCN-NY: {bcn.midpoint_to(ny).to_degrees()}")
    print(f"BCN-NY: {bcn.midpoint_to(paris).to_degrees()}")
    
    print(F"Counter: {Location.count()}")

    print("*" * 150)
    print("*" * 150)
    coord = Location(name = "5", latitude = 85.0, longitude = 15.0)
    print("*" * 150)
    print("*" * 150)
    
    print("*" * 150)
    print("*" * 150)
    
    print(F"RGB Limits: ({Color.MIN_VALUE},{Color.MAX_VALUE})")
    c1 = Color(name="Black", red=0, green=0, blue=0)
    c2 = Color(name="White", red=255, green=255, blue=255)
    c3 = Color(name="Black", red=0, green=0, blue=0)
    c4 = Color(name="Black", red=0, green=0, blue=0)
    c5 = Color(name="White", red=255, green=255, blue=255)
    c6 = Color.random()
    c7 = Color.random()
    c8 = Color.from_hex("#FF00FF")
    c9 = Color.from_hex("#FF05F5")
    c10 = AlphaColor(name= "My Color #1", red = 255, green= 255, blue=255, alpha = 50)
    c11 = AlphaColor(name= "My Color #2", red = 255, green= 255, blue=255, alpha = 10)

    colors = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11)
    for color in colors:
        print("-" * 150)
        print(color)
        print(f"Color: {color.to_hex()}")
        print(f"Color: {color.to_rgb()}")
        print("-" * 150)
    
    print(F"Counter: {Color.count()}")


    print("*" * 150)
    print("*" * 150)
    print("*" * 150)
    color1 = Color("Black", 0, 0, 0)
    color2 = Color("Black", 0, 0, 0)
    print(color1)
    print(hex(id(color1)))
    print(color2)
    print(hex(id(color2)))
    print(color1 == color2)
    print(color1 is color2)
    
    loc1 = Location("XX", 45.0, 25.5)
    loc2 = Location("XX", 45.0, 25.5)
    print(loc1)
    print(loc2)
    print(loc1 == loc2)
    print(loc1 is loc2)

    print(bcn - mad)


    print("EVENTS")
    seconds = (60+1, 3600+1, (3600*24)+1, (3600*24+1))
    for secs in seconds:
        [days, hours, minuts] = planning.seconds_to_dhm(secs)
        print(f"{secs} segons -> Days: {days} hours: {hours} minuts: {minuts}")
    
    print(datetime.now() - timedelta(hours=1))

    event1 = Event(name = "Event1", date = date(year=2022, month=3, day=21), start_time = datetime.time(hour=18, minute =0), end_time = datetime.time(hour=22, minut =0), description = "Event1 Description")
    event2 = Event(name = "Event2", date = date(year=2022, month=3, day=21), start_time = datetime.time(hour=18, minute =0), end_time = datetime.time(hour=22, minut =0), description = "Event2 Description")
    event3 = Event(name = "Event3", date = date(year=2022, month=3, day=21), start_time = datetime.time(hour=18, minute =0), end_time = datetime.time(hour=22, minut =0), description = "Event3 Description")
    event4 = Event(name = "Event4", date = date(year=2022, month=3, day=21), start_time = datetime.time(hour=18, minute =0), end_time = datetime.time(hour=22, minut =0), description = "Event4 Description")
    #event5 = Event(name = "Event5", date = datetime.now(), description = "Event5 Now Description")
    events =(event1,event2,event3,event4)

    for event in events:
        print(f"{event.name}: Duration: {event.duration()}")

if __name__ == "__main__":
    main()