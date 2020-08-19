""" exercise 15.2, Allen Downey, _Think Python_ 2nd ed.
"""

import turtle
from mypolygon import polyline, arc
from circle import Circle
from classes import Point, Rectangle


def draw_circle(t, c):
    t.pu()
    t.goto(c.center.x, c.center.y - c.radius)
    t.pd()
    arc(t, c.radius, 360)
    t.pu()
    t.goto(0, 0)
    t.seth(0)

def draw_rectangle(t, rect):
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.pd()
    t.seth(0)
    
    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)

    t.pu()
    t.goto(0, 0)
    t.seth(0)


def main():
    c = Circle()
    c.center = Point()
    c.center.x = 0
    c.center.y = 0
    c.radius = 100

    rect = Rectangle()
    rect.corner = Point()
    rect.corner.x = -100
    rect.corner.y = 100
    rect.width = 200
    rect.height = 300

    bob = turtle.Turtle()
    draw_circle(bob, c)
    draw_rectangle(bob, rect)
    turtle.mainloop()

if __name__ == '__main__':
    main()
