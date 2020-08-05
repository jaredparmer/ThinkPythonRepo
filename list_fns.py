import time

def load_words_append(filename):
    fin = open(filename)
    dict_list = []
    for line in fin:
        word = line.strip()
        dict_list.append(word)
    return dict_list

def load_words_concat(filename):
    fin = open(filename)
    dict_list = []
    for line in fin:
        word = line.strip()
        dict_list = dict_list + [word]
    return dict_list

def chop(t):
    del t[0]
    del t[-1]

def cumsum(t):
    cumsum = 0
    u = []
    for i in range(len(t)):
        cumsum += t[i]
        u.append(cumsum)
    return u

def has_duplicates(t):
    so_far = []
    for element in t:
        if element in so_far:
            return True
        so_far.append(element)
    return False

def is_anagram(a, b):
    t = list(a)
    u = list(b)
    t.sort()
    u.sort()
    return t == u

def is_sorted(t):
    u = t[:]
    u.sort()
    return t == u

def middle(t):
    return t[1:-1]

# takes a list of lists and adds up the elements from all the nested lists
def nested_sum(t):
    total = 0
    for i in range(len(t)):
        total += sum(t[i])
    return total

""" speed tests for loading words into lists
print("loading dictionary with append...")
t0 = time.time()
u = load_words_append('words.txt')
t1 = time.time()
print(f"finished! that took {(t1 - t0):.10f} seconds.")

print("loading dictionary with concatenation...")
t0 = time.time()
u = load_words_concat('words.txt')
t1 = time.time()
print(f"finished! that took {(t1 - t0):.10f} seconds.")
"""
