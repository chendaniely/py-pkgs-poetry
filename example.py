from collections import Counter

words = ["a", "happy", "hello", "a", "world", "happy"]
word_counts = Counter(words)
word_counts

with open("zen.txt") as file:
    text = file.read()

len(text)

text[0]

text = text.lower()

from string import punctuation

for p in punctuation:
    text = text.replace(p, "")

words = text.split()
words

word_counts = Counter(words)

def load_text(input_file):
        """Load text from a text file and return as a string."""
        with open(input_file, "r") as file:
            text = file.read()
        return text

def clean_text(text):
        """Lowercase and remove punctuation from a string."""
        text = text.lower()
        for p in punctuation:
            text = text.replace(p, "")
        return text

def count_words(input_file):
        """Count unique words in a string."""
        text = load_text(input_file)
        text = clean_text(text)
        words = text.split()
        return Counter(words)

