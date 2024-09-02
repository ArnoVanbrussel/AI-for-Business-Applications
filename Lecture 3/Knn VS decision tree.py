
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
for i in range(len(y_test)):
    true_label = y_test[i]
    predicted_label = y_pred[i]
    is_correct = predicted_label == true_label
    print(f"Predicted: {predicted_label}, True: {true_label}, Correct: {is_correct}")
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
for i in range(len(y_test)):
    true_label = y_test[i]
    predicted_label = y_pred[i]
    is_correct = predicted_label == true_label
    print(f"Predicted: {predicted_label}, True: {true_label}, Correct: {is_correct}")
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

