"""
# Linear Regression From Scratch
# Generate synthetic data:
# X: 200 samples, 1 feature (random)
# y = 3*X + 5 + noise
# Fit using closed-form normal equation (no sklearn).
# Print estimated slope and intercept.
"""

import numpy as np

X=np.random.rand(200,1)

#Gaussian (normal) noise:
sigma = 0.4   # noise strength
noise = np.random.randn(200, 1) * sigma 
y = 3*X+5+noise

# Normal equation formula  θ=(XT*X)−1 XT*y
X_b = np.c_[np.ones((200, 1)), X]     #Bias to the X
theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
intercept, slope = theta.ravel()

print("Intercept:", intercept)
print("Slope:", slope)