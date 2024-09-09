import datetime
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.covariance import GraphicalLassoCV
from sklearn import cluster
import yfinance as yf

# Input file containing company symbols
input_file = 'company_symbol_mapping.json'

# Load the company symbol map
with open(input_file, 'r') as f:
    company_symbols_map = json.loads(f.read())

symbols, names = np.array(list(company_symbols_map.items())).T

# Load the historical stock quotes
start_date = "2021-01-01"
end_date = "2021-12-31"

# Initialize lists to store opening and closing quotes
opening_quotes = []
closing_quotes = []
dates = None

# Fetch historical data for each stock symbol
valid_symbols = []  # Store symbols with valid data
for symbol in symbols:
    data = yf.Ticker(symbol).history(start=start_date, end=end_date)
    
    if data.empty or len(data) < 2:
        continue
    
    # Extract dates if not already extracted
    if dates is None:
        dates = data.index
    
    # Check if the data aligns with existing dates
    if not np.array_equal(dates, data.index):
        continue

    opening_quotes.append(data["Open"].values)
    closing_quotes.append(data["Close"].values)
    valid_symbols.append(symbol)

# Convert lists to NumPy arrays
opening_quotes = np.array(opening_quotes)
closing_quotes = np.array(closing_quotes)

# Compute differences between opening and closing quotes
quotes_diff = closing_quotes - opening_quotes

# Normalize the data
X = quotes_diff.T
X = np.nan_to_num(X)  # Replace NaN with 0 (you can choose another value if needed)

# Create a graph model (GraphicalLassoCV)
edge_model = GraphicalLassoCV()

# Train the model
with np.errstate(invalid='ignore'):
    edge_model.fit(X)

# Build clustering model using Affinity Propagation model
_, labels = cluster.affinity_propagation(edge_model.covariance_)

# Ensure that labels match the valid symbols
matched_labels = np.zeros(len(symbols), dtype=int) - 1
for i, symbol in enumerate(symbols):
    if symbol in valid_symbols:
        matched_labels[i] = labels[valid_symbols.index(symbol)]

# Filter symbols and labels to match common indices
symbols = symbols[matched_labels >= 0]
labels = matched_labels[matched_labels >= 0]

# Print the results of clustering
num_labels = labels.max()
print('\nClustering of stocks based on difference in opening and closing quotes:\n')
for i in range(num_labels + 1):
    cluster_symbols = symbols[labels == i]
    print("Cluster", i+1, "==>", ', '.join(cluster_symbols))
