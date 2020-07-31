import math
from recursive_fns import factorial

def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1

def mysqrt(a):
    x = a / 2
    epsilon = 0.0000001
    while True:
        y = (x + a / x) / 2
        if x == y:
            break
        x = y
    return x

def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    for a in range(1, 10):
        my_est = mysqrt(a)
        math_est = math.sqrt(a)
        diff = abs(math_est - my_est)
        print(f"{a:3.1f}", end=' ')
        print(f"{my_est:.11f}", end=' ')
        print(f"{math_est:.11f}", end=' ')
        print(diff)

def eval_loop():
    while True:
        s = input("gimme something ('done' when done) > ")
        if s == 'done':
            break
        print(eval(s))

def estimate_pi():
    bar = 0
    factor = (2 * math.sqrt(2)) / 9801
    k = 0
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k)**4 * 396**(4 * k)
        term = num / den
        bar += term
        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / (bar * factor)
