'''
Planning Utilities and Entities
'''
import datetime as dt

from numpy import integer
from pylib.entities import geometry
from pylib.utils import strutils

from pylib.utils import strutils
from pylib.entities.geometry import Color
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


def seconds_to_dhm(seconds: int)-> tuple[int,int,int]:
    '''Convert seconds into --> (days,hours,minutes)'''
    days= seconds//86400
    hours= (seconds-(days*86400))//3600
    minuts= (seconds - ((days*86400) + (hours*3600)))//60
    return [days, hours, minuts]


#DATA TYPES (CLASS)
class Event():
    '''DocString'''    
    #ATRIBUTS a NIVELL DE CLASE
    MIN_TIME = dt.time(hour=0, minute=0)
    MAX_TIME = dt.time(hour=23, minute=59)
    DEFAULT_BACKGROUND_COLOR: 'Color' = Color.from_hex("#CCCCCC")
    DEFAULT_PUBLIC = True
    DEFAULT_DESCRIPTION = strutils.EMPTY

    #INICIALITZADOR CONTRUCTOR
    def __init__(self, name:str, date: dt.date, start_time: dt.time = MIN_TIME, end_time: dt.time = MAX_TIME, background_color: 'Color' = DEFAULT_BACKGROUND_COLOR, public: bool = True, description: str = strutils.EMPTY):
        '''DocString'''

        self.id:str = strutils.randcode()
        self.name:str = name
        self.date: dt.date = date
        self.start_time: dt.time = start_time
        self.end_time: dt.time = end_time
        self.background_color: 'Color' = background_color
        self.public: bool = public
        self.description: str = strutils.EMPTY

    #COMPORTAMIENTO: METODOS/OPERACIONES A NIVEL DE OBJETO O INSTANCIA

    def duration(self)-> tuple[int, int]:
        '''duration()    ---------> (hours, minutes)'''
        duration = self.end_time - self.start_time
        #return [f"{duration.hours:d%}", f"{duration.minuts:d%}"]
        return [duration.strptime(duration,"%H"),duration.strptime(duration,"%M")]

    def time_left(self)-> tuple[int, int, int]:
        '''time_left()   ---------> (days, hours, minutes)'''
        pass

    def time_passed(self) -> tuple[int, int, int]:
        '''time_passed() ---------> (days, hours, minutes)'''
        pass

    def upcoming(self) -> bool:
        '''upcoming()    ---------> bool'''
        pass
    
    def inprogress(self) -> bool:
        '''inprogress()  ---------> bool'''
        pass

    def finished(self) -> bool:
        '''finished()    ---------> bool'''
        pass    

    def is_before(self, other) -> bool:
        '''is_before(other) ------> bool'''
        pass

    def is_after(self, other) -> bool:
        '''is_after(other)  ------> bool'''
        pass

    def overloaps(self, other) -> bool:
        '''overloaps(other) ------> bool'''
        pass
    
    def sample(self, cls) -> 'Event':
        '''sample(cls)      ------> Event (@classmethod -> factory)'''
        pass
    
    # # MÉTODOS/OPERACIONES A NIVEL DE CLASE 
    # @classmethod
    # def random(cls) -> 'Location':
    #     """Python DocString"""
    #     return cls(name = "Random Localization", latitude = random.uniform(cls.MIN_LATITUDE, cls.MAX_LATITUDE), longitude = random.uniform(cls.MIN_LONGITUDE, cls.MAX_LONGITUDE))

    #datetime.combine


    def __str__(self) -> str:
        """__str__()"""
        return f"{self.id} > {self.name()}: {self.date} {self.start_time}-{self.end_time}. {self.description}"

    def __repr__(self):
        """__repr__() -> Mostra Event (nom, data i data inici)"""
        return f"{self.name},{self.date} {self.start_time}-{self.end_time}. {self.description}"

    def __len__(self) -> int:
        """__len__() -------------> minutes"""
        return self.end_time - self.start_time

    def __sub__(self,other: 'Event') -> tuple[int, int, int]:
        # """sub__(other) -------------> (days, hous, minutes) between two events"""
        if not isinstance(other, Event):
            raise TypeError("You can only sub with another Event")

        #start_time = self.start_time.strftime("%H:%M")
        #end_time = self.end_time.strftime("%H:%M")
        return [0,0,0]
    

    def __lt__(self, other: 'Event') -> bool:
        """__lt__(other)"""
        if not isinstance(other, Event):
            raise TypeError("You can only compare with another Event")
        return 

    def __le__(self, other: 'Event') -> bool:
        """__le__(other)"""
        if not isinstance(other, Event):
            raise TypeError("You can only compare with another Event")

        return 

    def __gt__(self, other: 'Event') -> bool:
        """__gt__(other)"""
        if not isinstance(other, Event):
            raise TypeError("You can only compare with another Event")

        return 

    def __ge__(self, other: 'Event') -> bool:
        """__ge__(other)"""
        if not isinstance(other, Event):
            raise TypeError("You can only compare with another Event")

        return 
