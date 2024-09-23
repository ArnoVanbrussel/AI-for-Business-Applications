import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Load the trained model
naive_bayes_classifier = joblib.load('naive_bayes_model.pkl')

# Load the TF-IDF vectorizer
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Preprocess function (same as before)
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    
    # Tokenization
    words = word_tokenize(text)
    
    # Remove stopwords and apply stemming
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    
    return " ".join(words)

# New review text (replace with your own review)
new_review_text = "This hotel was excellent, I had a great stay."

# Preprocess the new review text
preprocessed_text = preprocess_text(new_review_text)

# Use the TF-IDF vectorizer to transform the preprocessed text
input_data = tfidf_vectorizer.transform([preprocessed_text])

# Make a prediction using the trained model
predicted_rating = naive_bayes_classifier.predict(input_data)[0]

print("Predicted Rating:", predicted_rating)
