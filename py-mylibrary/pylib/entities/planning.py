'''
Planning Utilities and Entities
'''
import datetime as dt

JANUARY = 1
FEBRUARY = 2
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

def prev_leap_year(year: int = current_year()) -> int:
    '''Given a year shows the previous leap year. The default year is the actual one'''
    for prev_year in range(year-1, year-100, -1):
        if is_leap_year(prev_year):
            return prev_year
       
def next_leap_year(year: int = current_year()) -> bool:
    '''Given a year shows the previous leap year. The default year is the actual one'''
    for next_year in range(year+1, year+100, +1):
        if is_leap_year(next_year):
            return next_year

def total_days(year: int = current_year()) -> int:
    '''Return days of a year'''
    return 365 if not is_leap_year(year) else 366

def year_progress(pretty:bool = True, year: int = current_year()) -> float|str:
    '''Return % of the year'''
    progress = elapsed_days() / total_days()
    return f"{progress:.2%}" if pretty else progress * 100
    #raise NotImplementedError("Not yet implemented!!!")


# def seconds_to_dhm(seconds: int)-> tuple[int,int,int]:
#     #--> (days,hours,minutes)



#DATA TYPES (CLASS)
class Event:
    '''DocString'''    

    from pylib.utils import strutils
    from pylib.entities.geometry import Color

    #ATRIBUTS a NIVELL DE CLASE
    MIN_TIME = dt.datetime.strptime("00:00", "%H;%M")
    MAX_TIME = dt.datetime.strptime("23:59", "%H;%M")
    DEFAULT_BACKGROUND_COLOR: 'Color' = Color.to_hex("#CCCCCC")
    DEFAULT_PUBLIC = True
    DEFAULT_DESCRIPTION = strutils.EMPTY

    def __init__(self, id:str, name:str, date: dt.date, start_time: dt.time, end_time: dt.time, background_color: 'Color', public: bool, description: str) -> None:
        '''DocString'''
        # id:               str       (strlutils.randcode())<---
        # name:             str
        # date:             date
        # start_time:       time      <---Default: 00:00h
        # end_time:         time      <---Default: 23:59h
        # background_color: color     <---Default: #CCCCCC
        # public:           bool      <---Default: true
        # description:      str       <---Default: Empty String

    #INICIALITZADOR CONTRUCTOR

# id:               str       (strlutils.randcode())<---
# name:             str
# date:             date
# start_time:       time      <---Default: 00:00h
# end_time:         time      <---Default: 23:59h
# background_color: color     <---Default: #CCCCCC
# public:           bool      <---Default: true
# description:      str       <---Default: Empty String


    #COMPORTAMIENTO: METODOS/OPERACIONES A NIVEL DE OBJETO O INSTANCIA

# duration()    ---------> (hours, minutes)
# time_left()   ---------> (days, hours, minutes)
# time_passed() ---------> (days, hours, minutes)
# upcoming()    ---------> bool
# inprogress()  ---------> bool
# finished()    ---------> bool
# is_before(other) ------> bool
# is_after(other)  ------> bool
# overloaps(other) ------> bool
# sample(cls)      ------> Event (@classmethod -> factory)
# ----------------------------
# __str__()
# __repr__()
# __len__() -------------> minutes
# __sub__(other) -------------> (days, hous, minutes) between two events
# __lt__(other)
# __le__(other)
# __gt__(other)
# __ge__(other)

#datetime.combine