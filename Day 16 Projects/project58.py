import numpy as np

# 1. Define Inputs
input_vector = np.array([2, 3, 4])
print("Input Vector:")
print(input_vector)

# 2. Define Weights and Bias
weights_matrix = np.random.rand(3, 2)  # 3 inputs -> 2 output neurons
bias_vector = np.array([0.1, 0.2])

print("\nWeights Matrix (3x2):")
print(weights_matrix)
print("\nBias Vector:")
print(bias_vector)

# 3. Perform Linear Transformation: output = input_vector @ weights_matrix + bias_vector
linear_output = input_vector @ weights_matrix + bias_vector
print("\nLinear Output (Before Activation):")
print(linear_output)

# 4. Add Activation Function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

activated_output = sigmoid(linear_output)
print("\nActivated Output (After Sigmoid):")
print(activated_output)

# 5. Final Summary
print("\n=== Summary ===")
print("Input Vector:", input_vector)
print("Weights Matrix:\n", weights_matrix)
print("Bias Vector:", bias_vector)
print("Linear Output:", linear_output)
print("Activated Output:", activated_output)
