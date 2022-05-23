from pycounts_poetry.pycounts import count_words
from pycounts_poetry.plotting import plot_words

counts = count_words("zen.txt")

print(counts)

fig = plot_words(counts, 10)

import matplotlib.pyplot as plt

plt.show()
