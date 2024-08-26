from sklearn import datasets

a = datasets.fetch_california_housing()
print(a.target)

b = datasets.load_digits()
print(b.images[4])

c = datasets.load_iris()
print(c["DESCR"])