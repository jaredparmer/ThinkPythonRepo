""" this solves exercises 13.1 through 13.4 of Downey, _Think Python_ 2nd ed
"""

import string
from tuple_fns import sum_all


""" reads a text into a histogram dictionary that records each word used as
a key, and the frequency of the word as the value. Ignores header data from
files gotten from Project Gutenberg (http://gutenberg.org).
"""
def load_file(filename='lorem_ipsum.txt', gutenberg=False):
    d = {}
    strippables = string.whitespace + string.punctuation

    # preliminaries for Project Gutenberg texts
    if gutenberg:
        fin = open(filename, encoding='utf8')
        skip_gutenberg_header(fin)
    else:
        fin = open(filename)

    for line in fin:
        if gutenberg and line.startswith('*** END OF THIS'):
            break
        
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            d[word] = d.get(word, 0) + 1

def summarize_file(filename, d):
    total_count = sum_all(*d.values())
    total_words = len(d)
    t = d.items()

    print("Filename: " + filename)
    print("Total word count: " + str(total_count))
    print("Total words used: " + str(total_words))
    return d


# precondition: file is open
def skip_gutenberg_header(fin):
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break

filename = 'emma.txt'
d = load_file(filename, True)
summarize_file(filename, d)
