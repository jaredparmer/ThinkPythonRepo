# these functions solve exercise 12.3 of Allen Downey's _Think Python_ 2nd ed.

from dict_fns import load_words_dict
from anagram_sets import signature, anagram_dict

def metathesis_pairs(d):
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)

def word_distance(word1, word2):
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
            
    return count

d = anagram_dict()
metathesis_pairs(d)
