""" solves exercises from section 14.12 of Allen Downey, _Think Python_ 2nd ed.
"""

""" exercise 14.1. replaces given pattern string with replacement string for
all occurrences in given input file, and writes file with replacements to given
output file. implements excessive exception catching.
"""
def sed(pattern, replacement, finname, foutname):
    try:
        fin = open(finname)
    except:
        print(f"Error opening {finname} for reading.")
        return

    try:
        fout = open(foutname, 'w')
    except:
        print(f"Error opening {foutname} for writing.")
        return

    for line in fin:
        try:
            fout.write(line.replace(pattern, replacement))
        except:
            print(f"Error writing {line} to {foutname}.")
            return

    try:
        fin.close()
    except:
        print(f"Error closing {finname}.")
        return

    try:
        fout.close()
    except:
        print(f"Error closing {foutname}.")
        return


""" exercise 14.2.
"""
from anagram_sets import anagram_dict, signature
import shelve

def read_anagrams(word):
    sig = signature(word)
    with shelve.open('anagrams.db') as db:
        if sig not in db or len(db[sig]) == 1:
            print(f"Sorry, {word} has no anagrams.")
        else:
            print(f"anagrams for {word}:", end=' ')
            print(*(set(db[sig]) - set([word])), sep=', ')


def store_anagrams(filename='words.txt'):
    d = anagram_dict(filename)
    with shelve.open('anagrams.db') as db:
        for word, wordlist in d.items():
            db[word] = wordlist
