import math
import random

class KMeansEngine:
    """K-Means Clustering implementation using pure Python"""
    
    def __init__(self, n_clusters=3, max_iterations=100, tolerance=1e-6, random_state=42):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.random_state = random_state
        
        # Cluster centers and labels
        self.centroids = None
        self.labels = None
        self.fitted = False
        
        # Set random seed
        random.seed(random_state)
    
    def _euclidean_distance(self, point1, point2):
        """Calculate Euclidean distance between two points"""
        distance = 0
        for i in range(len(point1)):
            distance += (point1[i] - point2[i]) ** 2
        return math.sqrt(distance)
    
    def _initialize_centroids(self, X):
        """Initialize centroids randomly"""
        n_samples, n_features = len(X), len(X[0])
        
        # Find min and max values for each feature
        min_vals = [float('inf')] * n_features
        max_vals = [float('-inf')] * n_features
        
        for sample in X:
            for i in range(n_features):
                min_vals[i] = min(min_vals[i], sample[i])
                max_vals[i] = max(max_vals[i], sample[i])
        
        # Initialize centroids randomly within data range
        centroids = []
        for _ in range(self.n_clusters):
            centroid = []
            for i in range(n_features):
                value = random.uniform(min_vals[i], max_vals[i])
                centroid.append(value)
            centroids.append(centroid)
        
        return centroids
    
    def _assign_clusters(self, X):
        """Assign each point to the nearest centroid"""
        labels = []
        
        for sample in X:
            min_distance = float('inf')
            closest_cluster = 0
            
            for i, centroid in enumerate(self.centroids):
                distance = self._euclidean_distance(sample, centroid)
                if distance < min_distance:
                    min_distance = distance
                    closest_cluster = i
            
            labels.append(closest_cluster)
        
        return labels
    
    def _update_centroids(self, X, labels):
        """Update centroids based on current cluster assignments"""
        n_features = len(X[0])
        new_centroids = []
        
        for cluster_id in range(self.n_clusters):
            # Find all points in this cluster
            cluster_points = []
            for i, label in enumerate(labels):
                if label == cluster_id:
                    cluster_points.append(X[i])
            
            if cluster_points:
                # Calculate mean of cluster points
                centroid = []
                for feature_idx in range(n_features):
                    mean_value = sum(point[feature_idx] for point in cluster_points) / len(cluster_points)
                    centroid.append(mean_value)
                new_centroids.append(centroid)
            else:
                # Keep old centroid if cluster is empty
                new_centroids.append(self.centroids[cluster_id][:])
        
        return new_centroids
    
    def _centroids_changed(self, old_centroids, new_centroids):
        """Check if centroids have changed significantly"""
        for i in range(len(old_centroids)):
            distance = self._euclidean_distance(old_centroids[i], new_centroids[i])
            if distance > self.tolerance:
                return True
        return False
    
    def fit(self, X):
        """Fit K-Means clustering to data"""
        if not X or not X[0]:
            raise ValueError("Input data cannot be empty")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        n_samples = len(X)
        if n_samples < self.n_clusters:
            raise ValueError(f"Number of samples ({n_samples}) must be >= number of clusters ({self.n_clusters})")
        
        # Initialize centroids
        self.centroids = self._initialize_centroids(X)
        
        # K-Means iterations
        for iteration in range(self.max_iterations):
            # Assign points to clusters
            new_labels = self._assign_clusters(X)
            
            # Update centroids
            old_centroids = [centroid[:] for centroid in self.centroids]
            self.centroids = self._update_centroids(X, new_labels)
            
            # Check convergence
            if not self._centroids_changed(old_centroids, self.centroids):
                break
        
        self.labels = new_labels
        self.fitted = True
        return self
    
    def predict(self, X):
        """Predict cluster labels for new data"""
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        return self._assign_clusters(X)
    
    def fit_predict(self, X):
        """Fit the model and return cluster labels"""
        self.fit(X)
        return self.labels
    
    def get_centroids(self):
        """Get cluster centroids"""
        if not self.fitted:
            raise ValueError("Model must be fitted first")
        return [centroid[:] for centroid in self.centroids]