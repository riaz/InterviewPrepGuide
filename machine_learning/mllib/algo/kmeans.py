import numpy as np
import math
#from  mllib.algo.utils import euclidean_distance

def euclidean_distance(vec_1, vec_2):
    #a = np.array([1,2,3,4])
    #b = np.array([5,6,7,8])

    dist = 0
    for x, y in zip(vec_1, vec_2):
        dist += (x - y) ** 2
    return math.sqrt(dist)

class KMeans(object):
    """
    A simple clustering algorithm that forms k clusters by iterating re-assessing samples
    to the closest centroids and after that re-adjusts the centroids

    Parameters:
    k : int
        The number of clusters that the algorithm will form
    max_iterations: int
        The number of iterations that the algorithm will run 
    """

    def __init__(self, k=3, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
    
    def _initialize(self, X):
        """ Initialize k random centroids """
        n_samples, n_features = np.shape(X)
        
        # Note: centroids are points and will have the shape k * no_of_features
        centroids = np.zeros((self.k, n_features))

        for i in range(self.k):
            # pick up one of the elements  randomly            
            centroids[i] = X[np.random.choice(range(n_samples))]
        return centroids

    def _get_closest_centroid(self, sample, centroids):
        """
        Given a sample - compute the distance to each of the centroids and assign the closest as the 
        appropriate centroid for sample
        """
        closest_dst = float('inf')
        closest_centroid = 0

        for idx, centroid in enumerate(centroids):
            # we will compute an euclidean distance between the sample and centroid across its features
            dist = euclidean_distance(sample, centroid)
            if dist < closest_dst:
                closest_dst = dist
                closest_centroid = idx

        return closest_centroid
    
    def _create_clusters(self, centroids, X):
        """
        Here we will assing each sample in X to a centorid based on _get_closest_centroid     

        Note: the number of clusters is equal to number of centorids - shape (k * size_of_features)
        """

        clusters = [[] for _ in range(self.k)] 

        # note: these clusters are buckets where the data from X fits into 
        # i.e K clusters

        for sample_i, sample in enumerate(X):
            best_centroid = self._get_closest_centroid(sample, centroids)
            clusters[best_centroid].append(sample_i)
        return clusters
    
    def _calculate_centroids(self, clusters, X):
        """
        For this we will need to use the clusters which is mapping between k -> sample index, and X
        to combute the new centroids - vs the random one that initialize choose randomly
        """
        n_features = np.shape(X)[1]
        centroids = np.zeros((self.k, n_features))
        for i, cluster in enumerate(clusters):
            centroid = np.mean(X[cluster], axis=0)
            centroids[i] = centroid
        return centroids
    
    def _get_cluster_labels(self, clusters, X):
        """
        This methods classify the sample to predict their cluster 
        """
        y_pred = np.zeros(np.shape(X)[0])
        for cluster_id, cluster in enumerate(clusters):
            for sample_i in cluster:
                y_pred[sample_i] = cluster_id
        return y_pred

    def predict(self, X):
        """
        Putting it all together
        """

        # Initialize centroids as k random samples from X
        centroids = self._initialize(X)

        # iterate until convergence or upto max_iterations
        for _ in range(self.max_iterations):
            clusters = self._create_clusters(centroids, X)

            # persist the previous centrids
            # for an early exit 
            prev_centroids = centroids

            # Calculate new clusters from the actual data
            centroids = self._calculate_centroids(clusters, X)

            diff = centroids - prev_centroids
            
            if not diff.any():
                break

        return self._get_cluster_labels(clusters, X)


if __name__ == '__main__':
    data = np.random.rand(10,20)
    model = KMeans(k=5)
    labels = model.predict(data)
    print(labels)