import numpy as np

# 1. Define the function to calculate Euclidean distance
def euclidean_distance(v1, v2):
    return np.sqrt(np.sum((v1 - v2) ** 2))

# 2. Create sample vectors
v1 = np.array([2, 4, 5])
v2 = np.array([7, 1, 9])

print("Vector 1:", v1)
print("Vector 2:", v2)

# 3. Calculate the Euclidean Distance
distance = euclidean_distance(v1, v2)

# 4. Output the result
print("\nEuclidean Distance between the two vectors:")
print(distance)
