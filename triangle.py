def is_triangle(a, b, c):
    if a > (b + c):
        return False
    if b > (a + c):
        return False
    if c > (a + b):
        return False
    return True

def check_triangle():
    a = int(input("Length of side a: "))
    b = int(input("Length of side b: "))
    c = int(input("length of side c: "))

    if is_triangle(a, b, c):
        print("A triangle can be made out of those sides!")
    else:
        print("No triangle can be made out of those sides!")

check_triangle()
