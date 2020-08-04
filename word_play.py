def avoids(word, blacklist):
    for ch in blacklist:
        if ch in word:
            return False
    return True

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

# prints words with letter occurrences like this aabbcc at any point
def print_triple_doubles(filename):
    fin = open(filename)
    print("Triple-Double(s) Found:", end=' ')
    for line in fin:
        word = line.strip()
        # first, find all doubles in word
        doubles_list = []
        curr = 0
        prev = 0
        while curr < len(word):
            if curr != prev and word[curr] == word[prev]:
                doubles_list.append(prev)
                prev = curr + 1
                curr = curr + 2
            else:
                prev = curr
                curr = curr + 1
        # next, compared indices of first ch of each found double
        first = 0
        second = 1
        third = 2
        while third < len(doubles_list):
            if (doubles_list[third] - doubles_list[second] == 2 and
                doubles_list[second] - doubles_list[first] == 2):
                print(word, end=' ')
                break
            third += 1
            second += 1
            first += 1

def uses_all(word, matchlist):
    return uses_only(matchlist, word)

def uses_only(word, whitelist):
    for ch in word:
        if ch not in whitelist:
            return False
    return True

print_triple_doubles('words.txt')
