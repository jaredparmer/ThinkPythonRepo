from list_fns import load_words_append as load_words

# precondition: t is sorted list of values, target is value to be found
def in_bisect(t, target):
    # verify we haven't run out of words to check
    if len(t) == 0:
        return False

    # wordlist not empty; so check middle word
    index = len(t) // 2
    if target == t[index]:
        # target word found!
        return True
    # word not found; recurse if there are more words to check
    while index != 0:
        if target < t[index]:
            # check first half of wordlist
            return in_bisect(t[:index], target)
        else:
            # check second half of wordlist
            return in_bisect(t[index + 1:], target)
    return False

t = load_words('words.txt')
t.sort()
target = input("Give me a word ('get me out!' to quit): ")

while target != 'get me out!':
    if in_bisect(t, target):
        print(f"Found it! '{target}' is a valid word.")
    else:
        print(f"Sorry, '{target}' is not a word!")
    target = input("Give me a word ('get me out!' to quit): ")

print("Have a good day!")
