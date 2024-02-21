import numpy as np

def print_array(a):
    print(a)

# question 1
# 1. Create a rank 2 (2D) array that resembles the matrix below.
# [[11 12 13 14]
#  [15 16 17 18]]
print(f'Question 1')
print_array(np.array([[11, 12, 13, 14], [15, 16, 17, 18] ]))
# Add more calls to print_array as needed
print(f'Question 2')

zero_arr = np.zeros((4,3))
print(zero_arr)

print(f'Question 3')
one_arr = np.ones((4,3))
print(one_arr)

print(f'Question 4')
range_arr = np.arange(4,14)
print(range_arr)

print(f'Question 4')
arr_values = np.array([0., 1.5, 3., 4.5])
print(arr_values)

print(f'Question 5')
arr_fours = np.full((2, 2), 4)
print(arr_fours)

print(f'Question 6i')

identity_matrix = np.eye(4)
print(identity_matrix)

print(f'Question 6ii')
diagonal_matrix = np.diag([10, 12])
print(diagonal_matrix)


print(f'Question 7')
random_array = np.random.uniform(0, 10, size=(3, 3))
print(random_array)


print(f'Question 8')
random_array233 = np.random.randint(10, 20, size=(3, 3))
print(random_array233)

print(f'Question 9i')
myArray = np.array([[11,12,13], [14,15,16], [17,18,19]])
subarray_a = myArray[0, :2]
print(subarray_a)

print(f'Question 9ii')
myArray[:2, :] = 0
print(myArray)

print(f'Question 10')
arr = np.arange(21)[::-1]
print(arr)

print(f'Question 11')
myArray2 = np.array([[11,12,13], [14,15,16]])
reshaped_array = myArray2.reshape(3, 2)
print(reshaped_array)

