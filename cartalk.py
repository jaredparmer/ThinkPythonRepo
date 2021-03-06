from str_fns import is_palindrome
from dict_fns import load_pronunciation_dict
from dict_fns import load_words_dict

# prints words with letter occurrences like this aabbcc at any point
def puzzler_1(filename):
    fin = open(filename)
    print("Triple-Double(s) Found:")
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
                print(word)
                break
            third += 1
            second += 1
            first += 1


""" solves the following Car Talk puzzler:

"I was driving on the highway the other day and I happened to notice my
odometer.  Like most odometers, it shows six digits, in whole miles only. 
So, if my car had 300,000 miles, for example, I'd see 3-0-0-0-0-0.

"Now, what I saw that day was very interesting. I noticed that the last 4
digits were palindromic; that is, they read the same forward as backward. 
For example, 5-4-4-5 is a palindrome, so my odometer could have read
3-1-5-4-4-5.

"One mile later, the last 5 numbers were palindromic. For example, it could 
have read 3-6-5-4-5-6.  One mile after that, the middle 4 out of 6 numbers 
were palindromic.  And you ready for this? One mile later, all 6 were 
palindromic!

"The question is, what was on the odometer when I first looked?"
"""
def puzzler_2():
    print("Palindromic Odometers: ")
    # this range isn't quite right since a leading zero (e.g., 012321) is valid
    # can fix with str.zfill(6) for all 0 <= i < 100000
    for i in range(100000, 999997):
        first = str(i)
        second = str(i + 1)
        third = str(i + 2)
        fourth = str(i + 3)
        if (is_palindrome(first[2:]) and
            is_palindrome(second[1:]) and
            is_palindrome(third[1:-1]) and
            is_palindrome(fourth)):
            print(first)


""" Identifies the age of the child when her age and the age of her parent
are palindromic, have been palindromic five times before, and can be
palindromic two more times, assuming the parent will not live beyond 120.
"""
def puzzler_3():
    print("The Many-Reversible Age of the Daughter:")
    # these two lists track, respectively, the differences found in palin-
    # dromic age pairs, and the number of times that difference shows up
    diff_list = []
    count_list= []

    # step one: fill the above two lists for all possible parent ages,
    # assuming no parent lives past 120
    for parent in range(1, 121):
        # the child's age is set to the palindromic age of the parent
        child = child_age(parent)

        # guardian: make sure child is younger than parent
        if child >= parent:
            continue
        diff = parent - child
        if diff in diff_list:
            # difference has already occurred; increase corresponding count
            index = diff_list.index(diff)
            count_list[index] = count_list[index] + 1
        else:
            # difference is new; add to list and add corresponding count of 1
            diff_list.append(diff)
            count_list.append(1)

    # step two: find difference with exactly 8 occurrences, assuming there
    # will only be at most one such difference
    magic_diff = -1
    for i in count_list:
        if count_list[i] == 8:
            magic_diff = diff_list[i]

    # step three: recover parents with magic_diff, pick 6th, recover child age
    if magic_diff == -1:
        print("No solution!")
    else:
        magic_count = 0
        for parent in range(1, 121):
            child = child_age(parent)
            # guardian: make sure child is younger than parent
            if child >= parent:
                continue
            if parent - child == magic_diff:
                magic_count += 1
                if magic_count == 6:
                    print(child)


""" helper function for puzzler_3() that returns the age of a child that is
palindromic of the given parent age, as an int
"""
def child_age(parent):
    return int(str(parent)[::-1])


def puzzler_4():
    word_dict = load_words_dict()
    pron_dict = load_pronunciation_dict()
    found = 0

    for word in word_dict:
        word_1 = word[1:]
        word_2 = word[0] + word[2:]
        if (word_1 in word_dict and 
            word_2 in word_dict and
            homophones(word, word_1, pron_dict) and
            homophones(word, word_2, pron_dict)):
            found += 1
            if found == 1:
                print("Super homophonic words found:")
            print(word, word_1, word_2)

    if found == 0:
        print("No super homophonic words found! :(")


""" helper function for puzzler_4(). This function is 'dumb' in that it will
say the same word is a homophone with itself. The caller should thus pre-
screen the words for identity. Importantly, the CMU pronunciation dictionary
stores words with multiple pronunciations as distinct words (e.g., 'abdomen'
and 'abdomen(1)'), so identity cannot be straightforwardly checked with '=='.
"""
def homophones(word1, word2, pron_d):
    if word1 not in pron_d or word2 not in pron_d:
        return False
    return pron_d[word1] == pron_d[word2]


""" this solves exercise 12.4 from Downey's _Think Python_ 2nd ed. It finds the
longest reducible English word. See helper function is_reducible for defn of
reducibility.
"""
def puzzler_5():
    d = load_words_dict()
    # add single-letter words and empty string to d
    d[''] = None
    d['i'] = None
    d['a'] = None

    reducibles = []
    for word in d:
        if is_reducible(word, d):
            reducibles.append((len(word), word))

    reducibles.sort(reverse=True)
    print("Here are the ten longest reducible words:")
    for i in range(10):
        print(reducibles[i])

""" helper function for puzzler_5(). Takes a given parent word and computes a
list of all the children words that can be formed by removing one letter.
"""
def get_children(parent, d):
    children = []
    for i in range(len(parent)):
        candidate = parent[:i]
        if i < len(parent) - 1:
            candidate += parent[i+1:]
        if candidate in d:
            children.append(candidate)

    return children


""" helper function for puzzler_5(). a word is 'reducible' if a single letter
can be removed from it (from anywhere in the word) to produce a new valid word,
which is itself reducible. The empty string is reducible and is the base case.
This function is memoized.
"""
known = {}
def is_reducible(word, d):
    if word in known:
        return known[word]
    if len(word) == 0:
        # base case: the empty string is reducible
        known[word] = True
        return known[word]

    # recursion case: the word is reducible if one of its children is
    children = get_children(word, d)
    for child in children:
        if is_reducible(child, d):
            known[word] = True
            return known[word]

    # word is not base case and none of children are reducible
    known[word] = False
    return known[word]
