import numpy as np

# 1. Create Raw Data
students = [
    ["Alice", 85, 90],
    ["Bob", 78, 82],
    ["Charlie", 92, 88],
    ["David", 70, 75]
]

print("Original Raw Data:")
for row in students:
    print(row)

# 2. Convert numerical part to NumPy matrix
# Extract only numeric columns (math and science scores)
scores = np.array([row[1:] for row in students])

print("\nNumeric Matrix (Math, Science):")
print(scores)

# 3. Perform Operations

# (a) Add a new feature: sports_score
sports_score = np.array([[80], [75], [95], [65]])  # a column vector
scores_with_sports = np.hstack((scores, sports_score))

print("\nAfter Adding Sports Score Column:")
print(scores_with_sports)

# (b) Calculate a new feature: average_score
average_score = np.mean(scores_with_sports, axis=1).reshape(-1, 1)
scores_with_avg = np.hstack((scores_with_sports, average_score))

print("\nAfter Adding Average Score Column:")
print(scores_with_avg)

# (c) Scale a feature: increase math score by 10%
scaled_scores = scores_with_avg.copy()
scaled_scores[:, 0] = scaled_scores[:, 0] * 1.1  # scale first column (math)

print("\nAfter Scaling Math Scores by 10%:")
print(scaled_scores)

# 4. Output all transformations clearly
print("\n=== Summary ===")
print("Original Matrix:\n", scores)
print("\nWith Sports and Average:\n", scores_with_avg)
print("\nAfter Scaling Math:\n", scaled_scores)
