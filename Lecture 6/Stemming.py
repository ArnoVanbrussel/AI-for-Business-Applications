import nltk
from nltk.stem import SnowballStemmer

# Initialize the Snowball stemmer for English
snowball_stemmer = SnowballStemmer("english")

# List of words to stem
words = ["running", "eating", "adjustable", "jumped", "jumps"]

# Stem each word and print the results
stemmed_words = [snowball_stemmer.stem(word) for word in words]

print("Original words:", words)
print("Stemmed words:", stemmed_words)



