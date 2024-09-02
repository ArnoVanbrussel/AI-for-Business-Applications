
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

categories = ['sci.med', 'soc.religion.christian', 'comp.graphics', 'rec.sport.baseball']
data = fetch_20newsgroups(categories=categories)

X = data.data
y = data.target

# Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Predicted labels:", y_pred)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


