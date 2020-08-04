from str_fns import is_palindrome

# prints words with letter occurrences like this aabbcc at any point
def puzzler_1(filename):
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
    print("solutions to the puzzler: ")
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

def puzzler_3():

