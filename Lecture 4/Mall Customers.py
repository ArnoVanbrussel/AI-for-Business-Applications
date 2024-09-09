import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, KMeans, estimate_bandwidth
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA

data = pd.read_csv('Mall_Customers.csv')

# Encode the "Gender" column using one-hot encoding
encoder = OneHotEncoder(sparse=False)
gender_encoded = encoder.fit_transform(data[['Gender']])

X = np.concatenate((data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].values, gender_encoded), axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Use Mean Shift to determine the number of clusters
bandwidth = estimate_bandwidth(X_scaled, quantile=0.1, n_samples=len(X_scaled))
meanshift = MeanShift(bandwidth=bandwidth)
meanshift.fit(X_scaled)

# Determine the number of clusters based on Mean Shift
n_clusters = len(np.unique(meanshift.labels_))
print(f"Estimated number of clusters using Mean Shift: {n_clusters}")

# Perform K-Means clustering with the estimated number of clusters
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

# Add cluster labels to the original dataset
data['Cluster'] = kmeans.labels_

# Reduce dimensionality for visualization (you can skip this if you prefer not to visualize)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
data['PCA1'] = X_pca[:, 0]
data['PCA2'] = X_pca[:, 1]

# Visualize the clusters using a scatter plot (2D PCA projection)
plt.figure(figsize=(10, 8))
for cluster in range(n_clusters):
    plt.scatter(data[data['Cluster'] == cluster]['PCA1'],
                data[data['Cluster'] == cluster]['PCA2'],
                label=f'Cluster {cluster}', alpha=0.7)

plt.title('K-Means Clustering Results')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.grid()
plt.show()

# Print cluster centroids
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
print('Cluster Centers (Age, Annual Income (k$), Spending Score (1-100), Gender Female, Gender Male):')
print(cluster_centers)

# Organize the data by clusters
clustered_data = []
for cluster in range(5):
    cluster_data = data[data['Cluster'] == cluster].copy()
    clustered_data.append(cluster_data)

# Display data in each cluster
for cluster, cluster_data in enumerate(clustered_data):
    print(f'\nCluster {cluster}:\n')
    print(cluster_data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender']])
