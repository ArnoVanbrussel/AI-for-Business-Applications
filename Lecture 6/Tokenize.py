import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Sample sentences for tokenization
sample_text = "Hello, Mr. Smith. How are you today? I hope you're doing well. Have a great day!"

# Tokenize the sentences
sentences = sent_tokenize(sample_text)

# Print the tokenized sentences
for sentence in sentences:
    print(sentence)

