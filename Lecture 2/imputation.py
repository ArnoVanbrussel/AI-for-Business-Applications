import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Lecture 2/train.csv")
# df.fillna(df.median(), inplace=True)
# print(df.head(10))

x = df.iloc[:, 0:20]
x = x.fillna(x.median())
y = df.iloc[:, -1]
y = y.fillna(y.median())

model = ExtraTreesClassifier()
model.fit(x, y)
print(model.feature_importances_)
feat_importances = pd.Series(model.feature_importances_, index=x.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()