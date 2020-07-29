import turtle
import math
from mypolygon import arc

def flower(t, n=7, length=100):
    for i in range(n):
        arc(t, length, 360/n)
        t.lt(180 - 360/n)
        arc(t, length, 360/n)
        t.lt(180)

bob = turtle.Turtle()
flower(bob, 14, 100)
bob.pu()
bob.fd(200)
bob.pd()
flower(bob, 7, 75)
turtle.mainloop()
