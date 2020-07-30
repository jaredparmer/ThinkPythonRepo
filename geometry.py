import math

def distance_bt(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

""" returns the length of the hypotenus of the right triangle formed by
the given lengths of the other two legs
"""
def hypotenus_of(a=3, b=4):
    return math.sqrt(a**2 + b**2)

def area(radius):
    return math.pi * radius**2

""" takes the coordinates of the center of a circle (xc, yc) and a point
on the perimeter (xp, yp) and calculates the area of the circle
"""
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def main():
    a = int(input("give me a: "))
    b = int(input("give me b: "))
    print("the hypotenus is length", hypotenus_of(a, b))

if __name__ == '__main__':
    main()
