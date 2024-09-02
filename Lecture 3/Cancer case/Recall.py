import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Load the dataset
column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                'Normal Nucleoli', 'Mitoses', 'Class']

data = pd.read_csv("breast-cancer-wisconsin.data", names=column_names)

# Data processing
data.replace("?", np.nan, inplace=True)
data.dropna(inplace=True)

# Split data into features (X) and target (y)
X = data.drop('Class', axis=1)
y = data['Class']

# Split data into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train a logistic regression model
logreg_model = LogisticRegression()
logreg_model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = logreg_model.predict(X_test_scaled)

# Calculate the confusion matrix
confusion = confusion_matrix(y_test, y_pred)

# Extract values from the confusion matrix
true_negative, false_positive, false_negative, true_positive = confusion.ravel()

# Calculate recall (true positive rate)
recall = true_positive / (true_positive + false_negative)
print("Recall (True Positive Rate):", recall)
