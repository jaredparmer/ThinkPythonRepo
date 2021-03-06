import turtle
import math

# draws a square whose sides are of a given length
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

"""
This function draws a given number of lines (n) of given length (length), with
a given angle (angle, in degrees) between them.
"""
def polyline(t, n=8, length=100, angle=45):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

"""
this function deploys polyline to draw a complete polygon of given number of
sides (n), with each side of given length (length)
"""
def polygon(t, n=8, length=100):
    angle = 360.0 / n
    polyline(t, n, length, angle)

"""
This function deploys polyline to draw an approximation of an arc of a circle
of a given angle (angle) and radius (r). The arc is approximated utilizing
several small angles (step_angle) and sides (step_length), where the number of
angles (n) grows with the length of the arc to be drawn. 
"""
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 5) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

"""
this function draws a circle, deploying the function arc to essentially draw
an "arc" with an angle of 360 degrees and a given radius (r)
"""
def circle(t, r=50):
    arc(t, r, 360)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

def main():
    bob = turtle.Turtle()
    polygon(bob, 4, 100)
    polygon(bob, 7, 100)
    circle(bob, 100)
    arc(bob, 100, 90)
    turtle.mainloop()#

if __name__ == '__main__':
    main()
