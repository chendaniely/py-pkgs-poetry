# example script to simulate loading the installed package

from pycounts_poetry.pycounts import count_words
from pycounts_poetry.plotting import plot_words

counts = count_words("zen.txt")

print(counts)

fig = plot_words(counts, 10)

import matplotlib.pyplot as plt

plt.show()

# Unit testing bits

einstein_counts = {'insanity': 1, 'is': 1, 'doing': 1, 
                   'the': 1, 'same': 1, 'thing': 1, 
                   'over': 2, 'and': 2, 'expecting': 1,
                   'different': 1, 'results': 1}

quote = "Insanity is doing the same thing over and over and \
             expecting different results."

with open("pycounts/tests/einstein.txt", "w") as file:
        file.write(quote)

from pycounts_poetry.pycounts import count_words
from collections import Counter
expected = Counter({'insanity': 1, 'is': 1, 'doing': 1,
                        'the': 1, 'same': 1, 'thing': 1, 
                        'over': 2, 'and': 2, 'expecting': 1,
                        'different': 1, 'results': 1})
actual = count_words("pycounts/tests/einstein.txt")
assert actual == expected, "Einstein quote counted incorrectly!"
