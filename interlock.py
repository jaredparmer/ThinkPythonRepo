from list_fns import load_words_append as load_words
from inlist import in_bisect
import time

def find_interlocking_pairs(word_list):
    for word in word_list:
        evens = word[::2]
        odds = word[1::2]
        if in_bisect(word_list, evens) and in_bisect(word_list, odds):
            print(f"'{evens}' and '{odds}' interlock to form '{word}'")
    return pairs

def main():
    word_list = load_words('words.txt')
    word_list.sort()
    t0 = time.time()
    pairs = find_interlocking_pairs(word_list)
    t1 = time.time()

    print(f"Finished! {int(len(pairs) * (2/3))} interlocking words have been "
          f"found in {(t1 - t0):.2f} seconds.")

if __name__ == '__main__':
    main()
