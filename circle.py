""" solves exercise 15.1 from Downey, _Think Python_ 2nd ed.
"""

from classes import Point, Rectangle, distance

class Circle:
    """ attributes: center Point, radius integer.
    """

""" checks whether given Point lies within or on boundary of given Circle
"""
def pt_in_circle(p, c):
    return distance(p, c.center) <= c.radius

def rect_in_circle(rect, c):
    point = copy.copy(rect.corner)
    if not pt_in_circle(point, c):
        return False

    point.x += rect.width
    if not pt_in_circle(point, c):
        return False

    point.y -= rect.height
    if not pt_in_circle(point, c):
        return False

    point.x -= rect.width
    if not pt_in_circle(point, c):
        return False

    return True

def rect_circle_overlap(rect, c):
    point = copy.copy(rect.corner)
    if pt_in_circle(point, c):
        return True

    point.x += rect.width
    if pt_in_circle(point, c):
        return True

    point.y -= rect.height
    if pt_in_circle(point, c):
        return True

    point.x -= rect.width
    if pt_in_circle(point, c):
        return True

    return False
