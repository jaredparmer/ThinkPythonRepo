# exercises from chapter 8 of Downey, _Think Python_ 2nd ed.

def count(word, letter):
    count = 0
    for check in word:
        if check == letter:
            count += 1
    return count

def find(word, letter, start=0, end=-1):
    index = start
    if end == -1:
        # no end given; traverse entire string
        end = len(word)

    while index < end:
        if word[index] == letter:
            return index
        index += 1

    return -1

def print_backwards(s):
    index = -1
    while index >= len(s) * (-1):
        print(s[index], end='')
        index -= 1

def is_palindrome(s):
    return s == s[::-1]

# implements Caesar cypher
def rotate(word, shift=1):
    shift_word = ''
    for c in word:
        # guardian: when c is not a letter, do not rotate
        if not c.isalpha():
            shift_c = c
        else:
            shift_place = ord(c) + shift
            # overflow handling:
            # character gets shifted past 'z' or 'Z',
            if c.islower() and shift_place > ord('z'):
                shift_place -= ord('z') - ord('a') + 1
            elif c.isupper() and shift_place > ord('Z'):
                shift_place -= ord('Z') - ord('A') + 1
            # or gets shifted to before 'a' or 'A'
            elif c.islower() and shift_place < ord('a'):
                shift_place += ord('z') - ord('a') + 1
            elif c.isupper() and shift_place < ord('A'):
                shift_place += ord('Z') - ord('A') + 1
            shift_c = chr(shift_place)
        shift_word += shift_c
    return shift_word
