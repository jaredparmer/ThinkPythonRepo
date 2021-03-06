import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def koch(t, length, n, angle):
    if length < 3:
        t.fd(length)
    else:
        koch(t, length / 3, n, angle)
        t.lt(angle)
        for i in range(n - 2):
            koch(t, length / 3, n, angle)
            t.rt(180 - angle)
        koch(t, length / 3, n, angle)
        t.lt(angle)
        koch(t, length / 3, n, angle)

def snowflake(t, length, n):
    # interior angle of polygon
    angle = ((n - 2) * 180) / n

    t.lt(angle)

    for i in range(n):
        koch(t, length, n, angle)
        t.rt(180 - angle)

    t.seth(0)

bob = turtle.Turtle()
bob.speed(0)
bob.pu()
bob.bk(200)
bob.pd()
snowflake(bob, 150, 5)
turtle.mainloop()
