from dict_fns import histogram

""" returns a list of tuples of frequency and character, sorted from most
frequent to least
"""
def most_frequent(s):
    s = s.lower()
    hist = histogram(s)
    t = []

    for x, freq in hist.items():
        if x.isalpha(): 
            t.append((freq, x))

    t.sort(reverse=True)
    return t

def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
