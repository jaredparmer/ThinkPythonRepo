""" solves exercise 13.8 of Downey, _Think Python_ 2nd ed. Performs Markov
analysis on a text.
"""

import string
import random
from word_freq import *


""" this function reads a text file, strips it of whitespace and punctuation,
and returns a dictionary as a Markov analysis of the text's contents, with
prefixes of given length as keys and lists of suffices as values.
"""
def analyze(filename='lorem_ipsum.txt', gutenberg=False, prefix_len=2):
    # step one: clean text and load into list
    # preliminaries for Project Gutenberg texts
    if gutenberg:
        fin = open(filename, encoding='utf8')
        skip_gutenberg_header(fin)
    else:
        fin = open(filename)

    word_list = []
    strippables = string.whitespace + string.punctuation + '“”'
    for line in fin:
        # check for end of Project Gutenberg text
        if gutenberg and line.startswith('*** END OF THIS'):
            break
        
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            word_list.append(word)

    # handle exceptions to bad prefix length
    if prefix_len < 1:
        raise IndexError("Prefix length is too small!")
    elif prefix_len >= len(word_list):
        raise IndexError("Prefix length is too large!")

    # step two: build dictionary
    analysis = {}
    for i in range(len(word_list) - prefix_len):
        # read next prefix and suffice
        prefix = word_list[i]
        for j in range(1, prefix_len):
            prefix = prefix + ' ' + word_list[j + i]
        suffix = word_list[i + prefix_len]
        
        # load into dict
        if prefix in analysis and suffix not in analysis[prefix]:
            analysis[prefix].append(suffix)
        else:
            analysis[prefix] = [suffix]

    return analysis


def generate(analysis, length=25):
    # pick start word
    prefix_list = list(analysis.keys())
    prefix = random.choice(prefix_list)
    print(prefix, end=' ')
    
    for i in range(length):
        suffix = random.choice(analysis[prefix])
        print(suffix, end=' ')
        prefix_slice = prefix.partition(' ')[2]
        prefix = prefix_slice + ' ' + suffix


""" helper function for analyze(). precondition: file is open
"""
def skip_gutenberg_header(fin):
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break


d = analyze('emma.txt', True, 3)
generate(d, 24)
