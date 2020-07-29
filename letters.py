import turtle
import math
from mypolygon import arc, move

def draw_a(t, height):
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.fd(height/2)
    t.lt(90)
    t.fd(height/2)
    t.lt(90)
    t.fd(height/2)
    t.lt(180)
    t.fd(height/2)
    t.lt(90)
    t.fd(height/2)
    t.lt(90)

def main():
    bob = turtle.Turtle()
    draw_a(bob, 50)
    move(bob, 100)
    draw_a(bob, 100)

    bob.hideturtle() 
    turtle.mainloop()

if __name__ == '__main__':
    main()
