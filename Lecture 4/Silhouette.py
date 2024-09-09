import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load the dataset with comma-separated values
data = pd.read_csv("data_clustering.txt", header=None)

# Convert the dataframe to a numpy array
data_array = data.values.astype(float)

# Estimate bandwidth (adjust quantile for tuning)
bandwidth = estimate_bandwidth(data_array, quantile=0.1)

# Create Mean Shift object and fit the data
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(data_array)

# Get cluster centers and labels
cluster_centers = ms.cluster_centers_
labels = ms.labels_

# Get the number of clusters
num_clusters = len(np.unique(labels))

print("Estimated number of clusters:", num_clusters)

# Compute the silhouette score
silhouette_avg = silhouette_score(data_array, labels)
print("Silhouette Score:", silhouette_avg)

# Plot the data points and cluster centers
plt.scatter(data_array[:, 0], data_array[:, 1], c=labels, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', s=200, linewidths=3, color='red', label='Cluster Centers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Mean Shift Clustering')
plt.show()
