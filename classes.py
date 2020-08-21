""" chapter 15 of Allen Downey, _Think Python_ 2nd ed.
"""

import math
import copy

class Point:
    """ represents a point in 2d space. """


class Rectangle:
    """ represents a rectangle.

    attributes: width, height, (top-left) corner (as a Point).
    """


class Time:
    """ represents time of day.

    attributes: hour, minute, second
    """


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
