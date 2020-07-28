import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

bob = turtle.Turtle()
#square(bob, 100)
#square(bob, 50)
#square(bob, 200)
polygon(bob, 4, 100)
polygon(bob, 3, 100)
polygon(bob, 8, 100)
turtle.mainloop()
