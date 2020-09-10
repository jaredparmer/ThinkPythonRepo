def avoids(word, blacklist):
    for ch in blacklist:
        if ch in word:
            return False
    return True

"""
with a generator expression.

def avoids(words, blacklist):
    return not any(letter in blacklist for letter in word)
"""

def has_no_e(word):
    return 'e' not in word

def is_abecedarian(word):
    word = word.lower()
    prev_ch = 'a'
    for ch in word:
        if ch < prev_ch:
            return False
        prev_ch = ch
    return True

def print_against_blacklist(filename):
    fin = open(filename)
    blacklist = input("Give me forbidden chars (no spaces!): ")
    print("Here are the words that have no forbidden characters:")
    for line in fin:
        word = line.strip()
        if avoids(word, blacklist):
            print(word, end=' ')
    print('\n')

def print_against_whitelist(filename):
    fin = open(filename)
    whitelist = input("Give me allowed chars (no spaces!): ")
    print("Here are the words that have only allowed characters:")
    for line in fin:
        word = line.strip()
        if uses_only(word, whitelist):
            print(word, end=' ')
    print('\n')

def print_e_free_words(filename):
    fin = open(filename)
    total = 0
    count = 0

    for line in fin:
        word = line.strip()
        if has_no_e(word):
            # print(word, end=' ')
            count += 1
        total += 1
    count_percent = (count / total) * 100
    print(f"Percentage of words containing no 'e': {count_percent}%")

def print_long_words(filename):
    fin = open(filename)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word, end=' ')
    print('\n')

def uses_all(word, matchlist):
    return uses_only(matchlist, word)

""" with a generator expression.

def uses_all(word, matchlist):
    return all(letter in matchlist for letter in word)
"""

def uses_only(word, whitelist):
    for ch in word:
        if ch not in whitelist:
            return False
    return True
