import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.covariance import GraphicalLassoCV
from sklearn import cluster
import json

# Define the stock symbols you want to analyze
stock_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "CGC", "BABA"]

# Load the company symbol map (you can create a JSON file for this)
company_symbols_map = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.",
    "AMZN": "Amazon.com Inc.",
    "TSLA": "Tesla Inc.",
    "CGC": "Canopy Growth Corporation",
    "BABA": "Alibaba Group Holding Limited"
}

# Extract opening and closing quotes for the specified date range
start_date = "2021-01-01"
end_date = "2021-12-31"

# Initialize lists to store opening and closing quotes
opening_quotes = []
closing_quotes = []

# Fetch historical data for each stock symbol
for symbol in stock_symbols:
    data = yf.Ticker(symbol).history(start=start_date, end=end_date)
    opening_quotes.append(data["Open"].values)
    closing_quotes.append(data["Close"].values)

# Convert lists to NumPy arrays
opening_quotes = np.array(opening_quotes)
closing_quotes = np.array(closing_quotes)

# Compute differences between opening and closing quotes
quotes_diff = closing_quotes - opening_quotes

# Normalize the data
X = quotes_diff.T
X /= X.std(axis=0)

# Create a graph model (GraphicalLassoCV)
edge_model = GraphicalLassoCV()

# Train the model
with np.errstate(invalid='ignore'):
    edge_model.fit(X)

# Build clustering model using Affinity Propagation model
_, labels = cluster.affinity_propagation(edge_model.covariance_)
num_labels = labels.max()

# Convert stock_symbols to a NumPy array
stock_symbols = np.array(stock_symbols)

# Print the results of clustering
print('\nClustering of stocks based on difference in opening and closing quotes:\n')
for i in range(num_labels + 1):
    cluster_symbols = stock_symbols[labels == i]
    print("Cluster", i+1, "==>", ', '.join(cluster_symbols))
