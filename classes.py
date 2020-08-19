""" chapter 15 of Allen Downey, _Think Python_ 2nd ed.
"""

import math
import copy

class Point:
    """ represents a point in 2d space. """


class Rectangle:
    """ represents a rectangle.

    attributes: width, height, corner (as a Point).
    """


""" calculates distance between two Point objects.
"""
def distance(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)


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
    

p1 = Point()
p2 = Point()
p1.x = 3.0
p1.y = 5.0
p2.x = 7.0
p2.y = -9.0

print(f"The difference between {point_str(p1)} and {point_str(p2)} "
      f"is {distance(p1, p2)}.")
