# import numpy package - for scientific computing
import numpy as np

# task 1 - create integer variable with value 100
hundred = 100
print("task 1: ", hundred)

# task 2 - create list (array) of numbers
num_list = [3, 4, 6, 8, 9]
print("\ntask 2: ", num_list)

# task 3 - create numpy array based on regular list from task #2
numpy_list = np.array(num_list)
print("\ntask 3: ", numpy_list)

# task 4 - create sequence of numbers from 5 to 15 (not including 15), default step is 1
sequence = np.arange(5, 15)
print("\ntask 4: ", sequence)

# task 5 - create sequence of numbers from 3 to 90 with NAMED parameter step=3
sequence2 = np.arange(3, 90, step=3)
print("\ntask 5: ", sequence2)

# task 6 - use numpy methods to create different matrices
matrix_rand = np.random.rand(3, 3)
matrix_zeroes = np.zeros(shape=(4, 10))
matrix_ones = np.ones((3, 3))
matrix_identity = np.identity(3)
matrix_eye = np.eye(5, 5, 1)
print("\ntask 6:")
print("random matrix:\n", matrix_rand)
print("\nmatrix with zeroes:\n", matrix_zeroes)
print("\nmatrix with ones:\n", matrix_ones)
print("\nidentity matrix:\n", matrix_identity)
print("\nmatrix eye:\n", matrix_eye)

# task 7 - create matrix filled with NaN (Not a Number)
matrix_nan = np.empty((3, 3))  # create matrix
matrix_nan[:] = np.nan  # fill matrix with NaN values
print("\ntask 7:\n", matrix_nan)

# task 8 - merge vectors into matrix
v1 = np.array([1, 2, 3, 4, 5, 6])  # create first vector (vector is just a 1 dimensional array)
v2 = np.array([7, 8, 9, 10, 11, 12])  # create second vector
matrix_merged = np.vstack((v1, v2))  # merge vectors into matrix
print("\ntask 8:")
print("first vector:\n", v1)
print("\nsecond vector:\n", v2)
print("\nmatrix merged:\n", matrix_merged)

# task 9 - use 'shape' property of array and 'reshape' method.
# 'shape' property shows the dimensions of matrix;
# in 'reshape' method the newshape product must be the same as product of an old shape
shape_of_matrix = matrix_merged.shape
print("\ntask 9:")
print("shape of matrix from task #8:\n", shape_of_matrix)

reshaped_matrix = np.reshape(matrix_merged, (4, 3))
print("\nreshape matrix from task #8 to shape (4, 3):\n", reshaped_matrix)

# task 10
print("\ntask 10:")
print("v1 + v2:\n", v1 + v2)
print("\nv1 - v2:\n", v1 - v2)
print("\nv1 * v2:\n", v1 * v2)
print("\nv1 ** 2:\n", v1 ** 2)
print("\nmatrix_merged * v1:\n", matrix_merged * v1)
print("\nv2 / v1:\n", v2 / v1)
print("\nnp.divide(v2, v1):\n", np.divide(v2, v1))
print("\nnp.dot(matrix_rand, matrix_identity):\n", np.dot(matrix_rand, matrix_identity))

# task 11
D = np.random.random((10, 10))
print("\ntask 11: ")
print("print D matrix:\n", D)
# !!! Note that counting is starting from 0, so by saying D[2, 3] the actual coordinates are [3, 4]
print("\nD[2, 3] - is the element in D matrix in position y=2, x=3 (counting from 0)\n", D[2, 3])
# ':' means that we should take ALL y-axis values, and '1' means we should take second value by x-axis.
print("\nD[:, 1] - is the second column in D matrix\n", D[:, 1])
