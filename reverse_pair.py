from list_fns import load_words_append as load_words
from inlist import in_bisect
import time

def find_reverse_pairs(t):
    pairs = []
    for i in range(len(t)):
        word = t[i]
        reverse_word = word[::-1]
        if reverse_word != word and in_bisect(t[i:], reverse_word):
            pairs.append(word)
            pairs.append(reverse_word)
    return pairs

def main():
    t = load_words('words.txt')
    t.sort()
    t0 = time.time()
    pairs = find_reverse_pairs(t)
    t1 = time.time()

    print(f"Finished! {len(pairs)} have been found in {t1 - t0} seconds.")
    print("Here are the first five pairs: ")
    for i in range(10):
        print(pairs[i])

if __name__ == '__main__':
    main()
