import numpy as np

arr1d = np.array([1, 2, 3])
print("1D Numpy Array: ", arr1d)

arr2d = np.array([[1, 2], [3, 4]])
print("2D Numpy Array: ", arr2d)

arr3d = np.array([[[1], [2]], [[3], [4]]])
print("3D Numpy Array: ", arr3d)

rand_arr = np.random.randint(1, 101, 10)
print("An array of 10 random integers: ", rand_arr)


zeros = np.zeros((2, 3))
print("Array of zeroes: ", zeros)

ones = np.ones((3, 2))
print("Array of ones: ", ones)

reshaped = np.arange(9).reshape(3, 3)
print("1D array of size 9 reshaped to 3x3: \n", reshaped)

second_row = reshaped[1]
print("Accessing second: ", second_row)
third_col = reshaped[:, 2]
print("Accessing third column: ", third_col)

a = np.array([1, 2, 3])
print("This is array a: ", a)
b = np.array([4, 5, 6])
print("This is array b: ", b)
add = a + b
print("Added array a and b: ", add)
sub = a - b
print("Subtracted array b from a: ", sub)
mul = a * b
print("Multiplied array a and b: ", mul)

mean_val = np.mean(a)
print("This is the mean of array a: ", mean_val)
median_val = np.median(a)
print("This is the median of array a: ", median_val)
std_val = np.std(a)
print("This is the standard deviation of array a: ", std_val)

filtered = rand_arr[rand_arr > 50]
print("Filtered array of 10 random integers: ", filtered)

flattened = reshaped.flatten()
print("Flattened 3x3 array: ", flattened)

broadcasted = a + 5
print("Broadcasted addition of 5 to every single element in array a: ", broadcasted)

identity = np.eye(4)
print("Identity matrix of size 4: ", identity)

matrix_5x5 = np.arange(1, 26).reshape(5, 5)
print("Generated a 5x5 matrix: \n", matrix_5x5)

arr = np.arange(1, 11)
arr[arr % 2 == 1] = -1
print("Replaced odd numbers in array of 1 to 10 with -1: ", arr)

diagonal = np.diag([10, 20, 30])
print("This is a diagonal matrix: \n", diagonal)

dot_prod = np.dot(a, b)
print("This is the dot product of a and b:", dot_prod)
