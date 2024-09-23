import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# load the data
sentence = "This is a simple example to demonstrate the removal of stop words."

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Get the list of stop words in English
stop_words = set(stopwords.words('english'))

# Remove stop words from the sentence
filtered_words = [word for word in words if word.lower() not in stop_words]

# Print the result
print("Original sentence:", sentence)
print("Filtered sentence:", ' '.join(filtered_words))


