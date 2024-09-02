import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                'Normal Nucleoli', 'Mitoses', 'Class']

data = pd.read_csv("breast-cancer-wisconsin.data", names=column_names)

data.replace("?", np.nan, inplace=True)
data.dropna(inplace=True) #pandas function that removes rows or columns with missing data


X = data.drop(['Class', 'Sample code number'], axis=1) #axis=1 specifies that a column (as opposed to a row) should be dropped
y = data['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

logreg_model = LogisticRegression()
logreg_model.fit(X_train_scaled, y_train)

y_pred = logreg_model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

model_filename = 'cancer_prediction_model.joblib'
joblib.dump(logreg_model, model_filename)
print("Model saved as", model_filename)


