# These functions solve exercise 12.2 of Allen Downey's _Think Python_ 2nd ed.


def signature(s):
    t = sorted(s)
    sig = ''.join(t)
    return sig


""" returns a dictionary of anagrams, where the keys are strings of alpha-
betically sorted characters, and the values are lists of words from the given
file that use exactly those characters and are anagrams of one another.
"""
def anagram_dict(filename='words.txt'):
    fin = open(filename)
    d = dict()
    
    for line in fin:
        word = line.strip()
        sig = signature(word)
        if sig not in d:
            d[sig] = [word]
        else:
            d[sig].append(word)

    return d


def filter_length(d, n):
    res = dict()
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


""" this function prints all sets of anagrams in the given dictionary, from
largest to smallest set.
"""
def print_all_anagrams(d):
    t = sort_anagram_dict(d)
    for i in t:
        print(i[1])


""" this function finds and prints the anagrams of the given string
"""
def print_anagrams(s, d):
    sig = signature(s)
    if sig not in d or len(d[sig]) == 1:
        print(f"Sorry! '{s}' has no anagrams.")
    else:
        print(f"The following are anagrams for '{s}':")
        for word in d[sig]:
            if word != s:
                print(word)


def sort_anagram_dict(d, descending=True):
    t = []
    for val in d.values():
        if len(val) > 1:
            t.append([len(val), val])
    t.sort(reverse=descending)
    return t


def main():
    d = anagram_dict()
    bingo = filter_length(d, 8)
    print_all_anagrams(bingo)

if __name__ == '__main__':
    main()
