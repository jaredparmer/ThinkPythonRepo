""" chapter 15 of Allen Downey, _Think Python_ 2nd ed.
"""

import math
import copy

class Point:
    """ represents a point in 2d space. """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, tuple):
            return self.add_tuple(other)
        elif isinstance(other, Point):
            return self.add_Point(other)
        else:
            raise TypeError('only tuples or Points can be added to a Point')

    def add_tuple(self, other):
        return Point(self.x + other[0], self.y + other[1])
    
    def add_Point(self, other):    
        return Point(self.x + other.x, self.y + other.y)

    """ allows Point object to be on right side of '+' operator
    """
    def __radd__(self, other):
        return self.__add__(other)


class Rectangle:
    """ represents a rectangle.

    attributes: width, height, (top-left) corner (as a Point).
    """


class Time:
    """ represents time of day.

    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def print_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

    def time_to_int(self):
        return self.second + self.minute*60 + self.hour*3600


def add_times(t1, t2):
    return int_to_time(time_to_int(t1) + time_to_int(t2))


""" calculates distance between two Point objects.
"""
def distance(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)


def increment(t, secs):
    return int_to_time(time_to_int(t) + secs)


""" takes a given number of seconds and returns a Time object with those
seconds partitioned into total hours, minutes, and seconds
"""
def int_to_time(secs):
    res = Time()
    res.minute, res.second = divmod(secs, 60)
    res.hour, res.minute = divmod(res.minute, 60)
    res.hour %= 24
    return res


def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


""" exercise 16.1 of Allen Downey, _Think Python_ 2nd ed.
"""
def mul_time(t, factor):
    return int_to_time(time_to_int(t) * factor)


""" moves Rectangle object by given values.
"""
def move(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


""" returns a copy of given Rectangle that is moved by given values.
"""
def move_w_copy(rect, dx, dy):
    result = copy.deepcopy(rect)
    move(result, dx, dy)
    return result


def point_str(p):
    return '(' + str(p.x) + ', ' + str(p.y) + ')'


def print_time(t):
    print(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}")


""" takes given Time object and returns its attributes as total seconds since
midnight
"""
def time_to_int(t):
    return t.second + t.minute*60 + t.hour*3600
