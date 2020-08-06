from list_fns import load_words_append as load_words_list
from inlist import in_bisect as list_search
import time

def histogram(str):
    d = dict()
    for ch in str:
        d[ch] = d.get(ch, 0) + 1
    return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val)
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def load_words_dict(filename):
    fin = open(filename)
    d = dict()
    for word in fin:
        word.strip()
        d[word] = 1
    return d

# precondition, given list t is sorted
def compare_searches(t, d):
    target = input("Give me a word ('get me out!' to quit): ")

    while target != 'get me out!':
        t0l = time.time()
        result_list = list_search(t, target)
        t1l = time.time()
        t0d = time.time()
        result_dict = target in d
        t1d = time.time()

        if result_list:
            print(f"{target} found in list, ", end='')
        else:
            print(f"{target} not found in list, ", end='')
        print(f"binary search time {t1l - t0l:.10f} secs")

        if result_dict:
            print(f"{target} found in dict, ", end='')
        else:
            print(f"{target} not found in dict, ", end='')
        print(f"dict search time {t1d - t0d:.10f} secs")

        target = input("Give me a word ('get me out!' to quit): ")

    print("Have a good day!")

def main():
    d = load_words_dict('words.txt')
    t = load_words_list('words.txt')
    t.sort()
    compare_searches(t, d)

if __name__ == '__main__':
    main()
