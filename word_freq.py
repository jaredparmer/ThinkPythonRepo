""" this solves exercises 13.1 through 13.7 of Downey, _Think Python_ 2nd ed
"""

import string
import random
from bisect import bisect
from dict_fns import load_words_dict as load_dict


""" takes a given histogram dictionary and chooses n words from it with a prob-
ability in proportion to that words's relative frequency. Returns n words as
a list.

precondition: given dictionary is a histogram: strings as keys and ints as
values, where the latter are interpreted to be frequencies of the former
"""
def choose_from_hist(d, n=1):
    weight_list = []
    words = d.keys()

    # construct weights for words
    total_count = sum(d.values())
    for word in d:
        word_weight = d[word] / total_count
        weight_list.append(word_weight)

    return random.choices(population=list(d.keys()), weights=weight_list, k=n)


""" exercise 13.7. Same as choose_from_hist but uses cumulative frequencies.
"""
def choose_from_hist_cum(d, n=1):
    word_list = []
    weight_list = []
    total_freq = 0

    for word, freq in d.items():
        word_list.append(word)
        total_freq += freq
        weight_list.append(total_freq)

    choices = []
    for i in range(n):
        x = random.randint(0, total_freq - 1)
        index = bisect(weight_list, x)
        choices.append(word_list[index])

    return choices
        

""" reads a text into a histogram dictionary that records each word used as
a key, and the frequency of the word as the value. Ignores header data from
files gotten from Project Gutenberg (http://gutenberg.org).
"""
def load_file(filename='lorem_ipsum.txt', gutenberg=False):
    words = {}
    strippables = string.whitespace + string.punctuation + '“”'

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
            words[word] = words.get(word, 0) + 1
    return words


""" helper function for print_most_common(). Gathers histogram dict into list
of tuples by frequency and by word, then sorts by most to least frequent.
"""
def most_common(hist):
    t = []
    for key, val in hist.items():
        t.append((val, key))
    t.sort(reverse=True)
    return t


""" helper function for summarize_file(). Prints n most common words and their
frequency.
"""
def print_most_common(d, n=20):
    t = most_common(d)
    print(f"The {n} most common words are:")
    for freq, word in t[:n]:
        print(word, freq, sep='\t')


""" helper function for summarize_file(). Identifies words in given histogram
dict that are not in given dictionary (filename).
"""
def print_not_in_dict(hist, filename='words.txt'):
    dictionary = load_dict(filename)
    not_in_dict = []

    for word in hist:
        if word not in dictionary:
            not_in_dict.append(word)

    print("Words not found in dictionary: " + str(len(not_in_dict)))
    answer = input("How many would you like to see? ('A' for all) ")
    if answer == 'A':
        n = len(not_in_dict)
    else:
        n = int(answer)

    for word in not_in_dict[:n]:
        print(word, end=' ')
    print('\n')


""" precondition: file is open
"""
def skip_gutenberg_header(fin):
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break


def summarize_file(words):
    total_count = sum(words.values())
    total_words = len(words)

    print("Total word count: " + str(total_count))
    print("Total words used: " + str(total_words), end='\n')
    print_most_common(words, 20)
    print_not_in_dict(words)


def main():
    filename = 'emma.txt'
    words = load_file(filename, True)
    summarize_file(words)
    sample_size = 100
    randoms = choose_from_hist_cum(words, sample_size)
    print(f"The following {sample_size} random words were chosen from the text:")
    for word in randoms[:sample_size]:
        print(word, end=' ')
    print('\n')


if __name__ == "__main__":
    main()
