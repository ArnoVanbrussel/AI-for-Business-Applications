import nltk
from nltk.stem import WordNetLemmatizer

# Initialize the WordNet lemmatizer for verb lemmatization
verb_lemmatizer = WordNetLemmatizer()

# List of words for verb lemmatization
words = ['gone', 'ate', 'liked', 'been', 'branded', 'writing']

# Lemmatize each word as verbs and print the results
lemmatized_verbs = [verb_lemmatizer.lemmatize(word, pos='v') for word in words]

print("Original words:", words)
print("Lemmatized verbs:", lemmatized_verbs)



