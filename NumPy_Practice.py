import numpy as np

print("NumPy Practice Session")
print("=" * 50)

# Exercise 1: Array Creation and Basic Stats
print("\n1. Array Creation and Basic Operations")
arr = np.random.randint(1, 21, size=(3, 4))
print(f"Random 3x4 array:\n{arr}")
print(f"Sum: {arr.sum()}")
print(f"Max: {arr.max()}, Min: {arr.min()}")
print(f"Row means: {arr.mean(axis=1)}")

# Exercise 2: Indexing and Slicing
print("\n2. Indexing and Slicing")
matrix = np.arange(1, 26).reshape(5, 5)
print(f"5x5 matrix:\n{matrix}")
print(f"Middle 3x3:\n{matrix[1:4, 1:4]}")
print(f"Every 2nd element from row 2: {matrix[2, ::2]}")

# Exercise 3: Boolean Operations
print("\n3. Boolean Indexing")
temps = np.array([23, 18, 31, 28, 15, 35, 12, 29, 26, 33])
print(f"Temperatures: {temps}")
hot_days = temps > 25
print(f"Hot days (>25°C): {temps[hot_days]}")
very_hot = temps > 30
temps_f = np.where(very_hot, temps * 9/5 + 32, temps)
print(f"With hot days in Fahrenheit: {temps_f}")

# Exercise 4: Array Manipulation
print("\n4. Array Reshaping")
arr1 = np.arange(1, 13)
arr2 = np.arange(13, 25)
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
mat1 = arr1.reshape(3, 4)
mat2 = arr2.reshape(3, 4)
stacked = np.vstack((mat1, mat2))
print(f"Stacked vertically:\n{stacked}")
final = stacked.reshape(8, 3)
print(f"Reshaped to 8x3:\n{final}")

# Exercise 5: Mathematical Operations
print("\n5. Mathematical Operations")
square_matrix = np.arange(1, 17).reshape(4, 4)
print(f"4x4 matrix:\n{square_matrix}")
sqrt_matrix = np.sqrt(square_matrix)
print(f"Square roots:\n{sqrt_matrix}")
transpose = square_matrix.T
print(f"Transpose:\n{transpose}")
dot_product = np.dot(square_matrix, transpose)
print(f"Dot product shape: {dot_product.shape}")

# Exercise 6: Statistics with Random Data
print("\n6. Statistical Analysis")
random_data = np.random.normal(50, 10, 1000)
print(f"Generated {len(random_data)} random numbers")
print(f"Mean: {random_data.mean():.2f}")
print(f"Median: {np.median(random_data):.2f}")
print(f"Std Dev: {random_data.std():.2f}")
percentiles = np.percentile(random_data, [25, 50, 75])
print(f"Percentiles (25th, 50th, 75th): {percentiles}")

# Exercise 7: Advanced Array Operations
print("\n7. Advanced Operations")
multiplication_table = np.outer(np.arange(6), np.arange(6))
print(f"6x6 multiplication table:\n{multiplication_table}")
perfect_squares = np.array([0, 1, 4, 9, 16, 25])
is_perfect_square = np.isin(multiplication_table, perfect_squares)
print(f"Perfect squares found: {np.sum(is_perfect_square)}")

# Exercise 8: Linear Algebra
print("\n8. Linear Algebra")
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))
print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"A + B:\n{A + B}")
print(f"Element-wise A * B:\n{A * B}")
print(f"Matrix multiplication A @ B:\n{A @ B}")

# Exercise 9: Array Searching and Sorting
print("\n9. Searching and Sorting")
unsorted = np.random.randint(1, 100, 15)
print(f"Unsorted array: {unsorted}")
sorted_arr = np.sort(unsorted)
print(f"Sorted: {sorted_arr}")
unique_vals = np.unique(unsorted)
print(f"Unique values: {unique_vals}")
max_index = np.argmax(unsorted)
print(f"Max value {unsorted[max_index]} at index {max_index}")

# Exercise 10: Broadcasting and Vectorization
print("\n10. Broadcasting")
matrix_3x4 = np.arange(12).reshape(3, 4)
row_vector = np.array([10, 20, 30, 40])
col_vector = np.array([[100], [200], [300]])
print(f"Original matrix:\n{matrix_3x4}")
print(f"Adding row vector {row_vector}:\n{matrix_3x4 + row_vector}")
print(f"Adding column vector:\n{matrix_3x4 + col_vector}")

print("\n" + "=" * 50)
print("NumPy practice session complete!")