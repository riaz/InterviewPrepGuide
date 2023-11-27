import numpy as np
from sklearn.metrics import pairwise_distances_argmin

class KMeans:
    def __init__(self, n_clusters=3, max_iter=300, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.cluster_centers_ = None

    def fit(self, X):
        if self.random_state:
            np.random.seed(self.random_state)
        
        # Randomly initialize the cluster centers
        initial_idx = np.random.permutation(X.shape[0])[:self.n_clusters]
        self.cluster_centers_ = X[initial_idx]

        for _ in range(self.max_iter):
            # Assign labels based on closest center
            labels = pairwise_distances_argmin(X, self.cluster_centers_)

            # Find new centers
            new_centers = np.array([X[labels == i].mean(axis=0) for i in range(self.n_clusters)])

            # Check for convergence
            if np.all(new_centers == self.cluster_centers_):
                break

            self.cluster_centers_ = new_centers


    def predict(self, X):
        return pairwise_distances_argmin(X, self.cluster_centers_)


if __name__ == '__main__':
    X = np.array([[1,2,3], [3,4,5], [5,6,7], [6,9,10]])
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)
    labels = kmeans.predict(X)
    print(labels)
