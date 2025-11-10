import numpy as np

# 1. Create a sample 2D dataset
# Rows = samples, Columns = features
M = np.array([
    [50, 80, 60],
    [60, 85, 65],
    [70, 78, 72],
    [65, 90, 68],
    [55, 82, 63]
])

print("Original Dataset (M):")
print(M)

# 2. Calculate Mean and Standard Deviation for each feature (column-wise)
mean = M.mean(axis=0)
std = M.std(axis=0)

print("\nFeature-wise Mean:")
print(mean)
print("\nFeature-wise Standard Deviation:")
print(std)

# 3. Perform Feature Scaling (Standardization)
# Formula: scaled = (M - mean) / std
M_scaled = (M - mean) / std

print("\nScaled Dataset (Z-Score Normalization):")
print(M_scaled)

# 4. Verify: Scaled data should have mean ~0 and std ~1
print("\nVerification:")
print("Means after scaling:", M_scaled.mean(axis=0))
print("Standard deviations after scaling:", M_scaled.std(axis=0))
