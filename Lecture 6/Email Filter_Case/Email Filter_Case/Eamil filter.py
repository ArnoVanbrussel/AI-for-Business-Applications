import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

# Load the data
data = pd.read_csv('Lecture 6/Email Filter_Case/Email Filter_Case/spam.csv')

# Text preprocessing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    # Tokenize the text and convert to lowercase
    words = word_tokenize(text.lower())
    
    # Remove stopwords and apply stemming (only to alphabetic tokens)
    words = [stemmer.stem(word) for word in words if word.isalpha() and word not in stop_words]
    
    return " ".join(words)

data['Message'] = data['Message'].apply(preprocess_text)

# Split the dataset into training and testing sets (80% train, 20% test)
X = data['Message']
y = data['Category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data to numerical data using TF-IDF
tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train) 
X_test_tfidf = tfidf_vectorizer.transform(X_test) 

# Train the Naive Bayes classifier
naive_bayes_classifier = MultinomialNB()
naive_bayes_classifier.fit(X_train_tfidf, y_train)
y_pred = naive_bayes_classifier.predict(X_test_tfidf)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')

# Function to classify a new review
def classify_new_review(new_review):
    preprocessed_review = preprocess_text(new_review)
    preprocessed_review_vectorized = tfidf_vectorizer.transform([preprocessed_review])
    category = naive_bayes_classifier.predict(preprocessed_review_vectorized)[0]
    return category

# Example usage:
new_review = "Please join the zoom meeting on time."
category = classify_new_review(new_review)
print(f"The category of the new review is: {category}")
