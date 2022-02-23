'''
Planning Utilities and Entities
'''
import datetime as dt

JANUARY = 1
FEBRERY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12


#CLASS LEVEL FUNCTIONS
def current_year() -> int:
    ''' Return the current year'''
    today = dt.date.today()
    return today.year

def elapsed_days() -> int:
    ''' Return the days passed the current year'''
    today = dt.date.today()
    first_day_current_year = dt.date(year = today.year, month = JANUARY, day =1)
    interval = today - first_day_current_year
    return interval.days + 1

def remaining_days() -> int:
    ''' Return the days to end the current year'''
    today = dt.date.today()
    last_day_current_year = dt.date(year = today.year, month = DECEMBER, day =31)
    interval = last_day_current_year - today
    return interval.days

def is_leap_year(year: int = current_year()) -> bool:
    '''Return if the year is leap'''
    
    #return (year % 4 == 0) and (year % 100 !=0 or year % 400 == 0)

    is_leap = False
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                is_leap_year = True
            else: is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False
    return is_leap_year

def prev_leap_year(year: int = current_year()) -> bool:
    pass
       
def next_leap_year(year: int = current_year()) -> bool:
    pass

def total_days(year: int = current_year()) -> int:
    '''Return days of a year'''
    return 365 if not is_leap_year(year) else 366

def year_progress(pretty:bool = True) -> float|str:
    '''Return % of the year'''
    progress = elapsed_days() / total_days()
    return f"{progress}:.2%" if pretty else progress * 100
    #raise NotImplementedError("Not yet implemented!!!")

#DATA TYPES (CLASS)
class Event:
    pass
