'''
Planning Utilities and Entities
'''
import calendar as c
from datetime import datetime, date, time
import math
from pylib.entities import geometry
from pylib.utils import mathutils, strutils
from pylib.entities.geometry import Color


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
    today = date.today()
    return today.year

def elapsed_days() -> int:
    ''' Return the days passed the current year'''
    today = date.today()
    first_day_current_year = date(year = today.year, month = JANUARY, day =1)
    interval = today - first_day_current_year
    return interval.days + 1

def remaining_days() -> int:
    ''' Return the days to end the current year'''
    today = date.today()
    last_day_current_year = date(year = today.year, month = DECEMBER, day =31)
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


def seconds_to_dhm(seconds: int)-> tuple[int,int,int]:
    '''Convert seconds into --> (days,hours,minutes)'''
    days= seconds//86400
    hours= (seconds-(days*86400))//3600
    minuts= (seconds - ((days*86400) + (hours*3600)))//60
    return [days, hours, minuts]


#DATA TYPES (CLASS)
class Event(object):
    '''Python DocString'''

    MIN_DURATION: int = 30
    NAME_MAX_LENGTH: int = 50
    DEFAULT_COLOR: 'Color' = Color.from_hex("#CCCCCC")

    def __init__(self, name: str, date: date, start_time: time = time(hour = 0, minute = 0, second = 0), end_time: time = time(hour = 23, minute = 59, second = 59), background_color: 'Color' = DEFAULT_COLOR, public: bool = True, description: str = strutils.EMPTY):
        """Python Docstring"""
        #------>[] Initalize state of object
        self._id = strutils.randcode(length = 6, digits = False)
        self.name = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.background_color = background_color
        self.public = public
        self.description = description  


    @property
    def id(self) -> str:
        """Python Docstring"""
        return self._id

    @property
    def name(self) -> str:
        """Python Docstring"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Python Docstring"""
        if not type(value) is str:
            raise TypeError(f"Attribute name must be of type str. You passed a {value.__class__.__name__}")

        self._name = value

    @property
    def date(self) -> date:
        """Python Docstring"""
        return self._date

    @date.setter
    def date(self, value: date):
        """Python Docstring"""
        if not type(value) is date:
            raise TypeError(f"Attribute date must be of type date. You passed a {value.__class__.__name__}")
        
        self._date = value

    @property
    def start_time(self) -> time:
        """Python Docstring"""
        return self._start_time

    @start_time.setter
    def start_time(self, value: time):
        """Python Docstring"""
        if not type(value) is time:
            raise TypeError(f"Attribute start_time must be of type time. You passed a {value.__class__.__name__}")
        
        self._start_time = value

    @property
    def end_time(self) -> time:
        """Python Docstring"""
        return self._end_time

    @end_time.setter
    def end_time(self, value: time):
        """Python Docstring"""
        if not type(value) is time:
            raise TypeError(f"Attribute end_time must be of type time. You passed a {value.__class__.__name__}")
        
        self._end_time = value

    @property
    def background_color(self) -> 'Color':
        """Python Docstring"""
        return self._background_color

    @background_color.setter
    def background_color(self, value: 'Color'):
        """Python Docstring"""
        if not type(value) is Color:
            raise TypeError(f"Attribute color must be of type Color. You passed a {value.__class__.__name__}")
       
        self._background_color = value

    @property
    def public(self) -> bool:
        """Python Docstring"""
        return self._public

    @public.setter
    def public(self, value: bool):
        """Python Docstring"""
        if not type(value) is bool:
            raise TypeError(f"Attribute public must be of type bool. You passed a {value.__class__.__name__}")
       
        self._public = value

    @property
    def description(self) -> str:
        """Python Docstring"""
        return self._description

    @description.setter
    def description(self, value: str):
        """Python Docstring"""
        if not type(value) is str:
            raise TypeError(f"Attribute description must be of type str. You passed a {value.__class__.__name__}")
       
        self._description = value



    def duration(self) -> tuple[int,int]:
        """Python Docstring"""
        interval = self._end_datetime() - self._start_datetime()
        (days, hours, minutes) = seconds_to_dhm(interval.total_seconds())
        return (hours, minutes)


    def time_left(self) -> tuple[int,int,int]:
        """Python Docstring"""
        now = datetime.now()
        interval = self._start_datetime() - now
        (days, hours, minutes) = seconds_to_dhm(interval.total_seconds())
        return (days, hours, minutes)

    def time_passed(self) -> tuple[int,int,int]:
        """Python Docstring"""
        now = datetime.now()
        interval = now - self._end_datetime()
        (days, hours, minutes) = seconds_to_dhm(interval.total_seconds())
        return (days, hours, minutes)

    def upcoming(self) -> bool:
        """Python Docstring"""
        now = datetime.now()
        return now < self._end_datetime()
    
    def inprogress(self) -> bool:
        """Python Docstring"""
        now = datetime.now()
        return now >= self._start_datetime() and now <= self._end_datetime()
    
    def finished(self) -> bool:
        """Python Docstring"""
        now = datetime.now()
        return now > self._end_datetime()
  
    def is_before(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self._start_datetime() < other._start_datetime()
    
    def is_after(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self._start_datetime() > other._start_datetime()

    def overloaps(self, other: 'Event') -> bool:
        """Python Docstring"""
        return (self._start_datetime() >= other._start_datetime() and self._start_datetime() <= other._end_datetime()) \
               or (self._end_datetime() >= other.start_time() and self._end_datetime() <= other._end_datetime())


    def _start_datetime(self) -> datetime:
        """Python Docstring"""
        return datetime.combine(date = self.date, time = self.start_time)
    
    def _end_datetime(self) -> datetime:
        """Python Docstring"""
        return datetime.combine(date = self.date, time = self.end_time)

    def __str__(self) -> str:
        """Python Docstring"""
        return f"{self.id} > {self.name}"

    def __repr__(self) -> str:
        """Python Docstring"""
        return f"{self.id} > {self.name}"

    def __len__(self) -> int:
        """Python Docstring"""
        interval = self._end_datetime() - self._start_datetime()
        return int(interval.total_seconds()/60)

    def __sub__(self, other: 'Event') -> tuple[int,int,int]:
        """Python Docstring"""
        diff = other._start_datetime() - self._start_datetime()
        (days,hours,minutes) = seconds_to_dhm(diff.total_seconds())
        return (days,hours,minutes)

    def __lt__(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self.is_before(other)

    def __le__(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self.is_before(other) or self._start_datetime() == other._start_datetime()

    def __gt__(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self.is_after(other)

    def __ge__(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self.is_after(other) or self._start_datetime() == other._start_datetime()
