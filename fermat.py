def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")

a = int(input('Give me a: '))
b = int(input('Give me b: '))
c = int(input('Give me c: '))
n = int(input('Give me n: '))

print(f"checking Fermat's Last Theorem with {a}, {b}, {c}, and {n}...")
check_fermat(a, b, c, n)
