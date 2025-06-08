import math
import random

class AutoencoderEngine:
    """Autoencoder Neural Network for dimensionality reduction and feature learning"""
    
    def __init__(self, input_dim, encoding_dim, learning_rate=0.01, max_epochs=1000, tolerance=1e-6):
        """
        Initialize Autoencoder
        input_dim: dimension of input data
        encoding_dim: dimension of encoded representation (bottleneck)
        """
        self.input_dim = input_dim
        self.encoding_dim = encoding_dim
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.tolerance = tolerance
        
        # Network weights: input -> encoding -> output
        self.encoder_weights = None
        self.encoder_bias = None
        self.decoder_weights = None
        self.decoder_bias = None
        
        self.fitted = False
        self.loss_history = []
        
        # Set random seed
        random.seed(42)
    
    def _xavier_initialization(self, fan_in, fan_out):
        """Xavier initialization for weights"""
        limit = math.sqrt(6.0 / (fan_in + fan_out))
        weights = []
        for i in range(fan_out):
            row = []
            for j in range(fan_in):
                weight = random.uniform(-limit, limit)
                row.append(weight)
            weights.append(row)
        return weights
    
    def _sigmoid(self, x):
        """Sigmoid activation function"""
        x = max(-250, min(250, x))
        return 1.0 / (1.0 + math.exp(-x))
    
    def _sigmoid_derivative(self, sigmoid_output):
        """Derivative of sigmoid"""
        return sigmoid_output * (1.0 - sigmoid_output)
    
    def _linear(self, x):
        """Linear activation (identity)"""
        return x
    
    def _forward_pass(self, x):
        """Forward pass through autoencoder"""
        # Encoder: input -> hidden
        encoded = []
        for i in range(self.encoding_dim):
            weighted_sum = self.encoder_bias[i]
            for j in range(self.input_dim):
                weighted_sum += x[j] * self.encoder_weights[i][j]
            encoded.append(self._sigmoid(weighted_sum))
        
        # Decoder: hidden -> output
        decoded = []
        for i in range(self.input_dim):
            weighted_sum = self.decoder_bias[i]
            for j in range(self.encoding_dim):
                weighted_sum += encoded[j] * self.decoder_weights[i][j]
            decoded.append(self._linear(weighted_sum))  # Linear output for reconstruction
        
        return encoded, decoded
    
    def _backward_pass(self, x, encoded, decoded):
        """Backward pass (backpropagation)"""
        # Calculate output error (reconstruction error)
        output_errors = []
        for i in range(self.input_dim):
            error = decoded[i] - x[i]
            output_errors.append(error)
        
        # Calculate hidden layer errors
        hidden_errors = []
        for i in range(self.encoding_dim):
            error = 0.0
            for j in range(self.input_dim):
                error += output_errors[j] * self.decoder_weights[j][i]
            # Apply derivative of activation function
            error *= self._sigmoid_derivative(encoded[i])
            hidden_errors.append(error)
        
        # Update decoder weights and biases
        for i in range(self.input_dim):
            for j in range(self.encoding_dim):
                gradient = output_errors[i] * encoded[j]
                self.decoder_weights[i][j] -= self.learning_rate * gradient
            self.decoder_bias[i] -= self.learning_rate * output_errors[i]
        
        # Update encoder weights and biases
        for i in range(self.encoding_dim):
            for j in range(self.input_dim):
                gradient = hidden_errors[i] * x[j]
                self.encoder_weights[i][j] -= self.learning_rate * gradient
            self.encoder_bias[i] -= self.learning_rate * hidden_errors[i]
    
    def fit(self, X, verbose=False):
        """Train the autoencoder"""
        # Convert single sample to matrix format
        if isinstance(X[0], (int, float)):
            X = [X]  # Single sample
        
        n_samples = len(X)
        
        # Set input dimension if not provided
        if self.input_dim is None:
            self.input_dim = len(X[0])
        
        # Initialize weights
        self.encoder_weights = self._xavier_initialization(self.input_dim, self.encoding_dim)
        self.encoder_bias = [0.0] * self.encoding_dim
        
        self.decoder_weights = self._xavier_initialization(self.encoding_dim, self.input_dim)
        self.decoder_bias = [0.0] * self.input_dim
        
        # Training loop
        self.loss_history = []
        prev_loss = float('inf')
        
        for epoch in range(self.max_epochs):
            total_loss = 0.0
            
            # Shuffle training data
            indices = list(range(n_samples))
            random.shuffle(indices)
            
            for idx in indices:
                sample = X[idx]
                
                # Forward pass
                encoded, decoded = self._forward_pass(sample)
                
                # Calculate reconstruction loss (Mean Squared Error)
                loss = 0.0
                for i in range(self.input_dim):
                    loss += (decoded[i] - sample[i]) ** 2
                loss /= self.input_dim
                total_loss += loss
                
                # Backward pass
                self._backward_pass(sample, encoded, decoded)
            
            avg_loss = total_loss / n_samples
            self.loss_history.append(avg_loss)
            
            if verbose and epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {avg_loss:.6f}")
            
            # Check convergence
            if abs(prev_loss - avg_loss) < self.tolerance:
                if verbose:
                    print(f"Converged at epoch {epoch}")
                break
            
            prev_loss = avg_loss
        
        self.fitted = True
        return self
    
    def encode(self, X):
        """Encode input data to lower dimensional representation"""
        if not self.fitted:
            raise ValueError("Autoencoder must be fitted before encoding")
        
        # Convert single sample
        if isinstance(X[0], (int, float)):
            X = [X]
        
        encoded_data = []
        for sample in X:
            encoded, _ = self._forward_pass(sample)
            encoded_data.append(encoded)
        
        return encoded_data[0] if len(encoded_data) == 1 else encoded_data
    
    def decode(self, encoded_X):
        """Decode encoded data back to original dimension"""
        if not self.fitted:
            raise ValueError("Autoencoder must be fitted before decoding")
        
        # Convert single sample
        if isinstance(encoded_X[0], (int, float)):
            encoded_X = [encoded_X]
        
        decoded_data = []
        for encoded_sample in encoded_X:
            # Decoder: encoded -> output
            decoded = []
            for i in range(self.input_dim):
                weighted_sum = self.decoder_bias[i]
                for j in range(self.encoding_dim):
                    weighted_sum += encoded_sample[j] * self.decoder_weights[i][j]
                decoded.append(self._linear(weighted_sum))
            decoded_data.append(decoded)
        
        return decoded_data[0] if len(decoded_data) == 1 else decoded_data
    
    def reconstruct(self, X):
        """Reconstruct input data (encode then decode)"""
        if not self.fitted:
            raise ValueError("Autoencoder must be fitted before reconstruction")
        
        # Convert single sample
        if isinstance(X[0], (int, float)):
            X = [X]
        
        reconstructed_data = []
        for sample in X:
            _, decoded = self._forward_pass(sample)
            reconstructed_data.append(decoded)
        
        return reconstructed_data[0] if len(reconstructed_data) == 1 else reconstructed_data
    
    def reconstruction_error(self, X):
        """Calculate reconstruction error for input data"""
        if not self.fitted:
            raise ValueError("Autoencoder must be fitted first")
        
        # Convert single sample
        if isinstance(X[0], (int, float)):
            X = [X]
        
        total_error = 0.0
        for sample in X:
            reconstructed = self.reconstruct([sample])
            error = 0.0
            for i in range(self.input_dim):
                error += (reconstructed[i] - sample[i]) ** 2
            total_error += error / self.input_dim
        
        return total_error / len(X)
    
    def get_encoding_weights(self):
        """Get encoder weights"""
        if not self.fitted:
            raise ValueError("Autoencoder must be fitted first")
        
        return [row[:] for row in self.encoder_weights]
    
    def get_loss_history(self):
        """Get training loss history"""
        return self.loss_history[:]