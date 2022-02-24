'''
Main module
'''

import math
import geography
import geometry
import mathutils
import planning
import strutils
import sysutils


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

if __name__ == "__main__":
    main()
    