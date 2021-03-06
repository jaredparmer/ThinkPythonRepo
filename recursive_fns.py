# calculates Ackermann function of two positive integers
# quickly exceeds recursion depth limits (whenever m > 3, e.g.)!
def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

# following three fns are helps for is_palindrome
# precondition: word is str
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# recursive function that checks non-empty strings
def is_palindrome(word):
    if len(word) <= 3:
        return first(word) == last(word)
    return is_palindrome(middle(word))

# a is a power of b iff it is divisible by b and a/b is a power of b
# precondition: both a and b are positive integers
def is_power(a, b):
    # base case 1: when b is 1, only 1 is a power of it 
    # base case 2: when a is 1, it is a power of any b
    if (b == 1 or a == 1):
        return a == 1
    
    if a % b != 0:
        return False
    return is_power(a / b, b)

def gcd(a, b):
    print(f"Checking {a}, {b}...")
    # guardian
    if a == 0 and b == 0:
        print("Two zeroes given. Terminating function.")
        return None

    # base cases: exactly one zero
    if a == 0:
        print("Exactly one zero received.")
        return b
    if b == 0:
        print("Exactly one zero received.")
        return a

    # recursion cases
    return gcd(b, a % b)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
