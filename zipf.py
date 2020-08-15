""" exercise 13.9 of Downey, _Think Python_ 2nd ed.
"""

from word_freq import load_file as load_hist
from word_freq import skip_gutenberg_header
import matplotlib.pyplot as plt


def rank_freq(hist):
    freqs = list(hist.values())
    freqs.sort(reverse=True)
    rf = [(r + 1, f) for r, f in enumerate(freqs)]
    return rf

hist = load_hist('emma.txt', True)
t = rank_freq(hist)
rs, fs = zip(*t)

plt.clf()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('log rank')
plt.ylabel('log frequency')
plt.plot(rs, fs, 'r-', linewidth=3)
plt.show()
