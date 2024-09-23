import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import joblib

# load dataset
df = pd.read_csv("Lecture 6/MovieReviews.csv")

# convert 'Rating' to numeric, force invalid parsing to NaN
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# drop rows with missing values in 'Rating' or 'Review' columns
df.dropna(subset=['Rating', 'Review'], inplace=True)

# text preprocessing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


def preprocess_text(text):
    # tokenization
    words = word_tokenize(text)

    # remove stopwords and apply stemming
    words = [stemmer.stem(word) for word in words if word not in stop_words]

    return " ".join(words)

df['Review'] = df['Review'].apply(preprocess_text)

def map_rating(rating):
    if rating > 6:
        return "positive"
    elif rating > 4:
        return "neutral"
    else:
        return "negative"

df['Sentiment'] = df['Rating'].apply(map_rating)

# split data into training and testing sets
X = df['Review']
y = df['Sentiment']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# convert text data to numerical features using TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# train a Naive Bayes classifier
naive_bayes_classifier = MultinomialNB()
naive_bayes_classifier.fit(X_train_tfidf, y_train)
y_pred = naive_bayes_classifier.predict(X_test_tfidf)

# evaluate model
accuracy = accuracy_score(y_test, y_pred)

# save trained model
joblib.dump(naive_bayes_classifier,'naive_bayes_model-movie.pkl')
joblib.dump(tfidf_vectorizer,'tfidf_vectorizer-movie.pkl')

print("Accuracy:", accuracy)