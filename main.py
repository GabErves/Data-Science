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

print(f'Question 12')
myArray3 = np.arange(10)
squared_array = np.square(myArray3)
print(squared_array)

print(f'Question 13')
sqrt_array = np.sqrt(myArray3)
print(sqrt_array)

print(f'Question 14')
multiplied_array = squared_array * sqrt_array
print(multiplied_array)

print(f'Question 15')
myArray4 = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
new_row = np.array([20, 21, 22])
myArray_with_new_row = np.append(myArray4, [new_row], axis=0)
print(myArray_with_new_row)

print(f'Question 16')
new_column = np.array([30, 40, 50])
myArray_with_new_column = np.append(myArray4, new_column.reshape(-1, 1), axis=1)
print(myArray_with_new_column)

print(f'Question 17')
myArray5 = np.zeros((2,2))
print(myArray5)

print(f'Question 18')
column_of_ones = np.ones((2,1))
myArray5 = np.hstack((myArray5, column_of_ones))
print(myArray5)

print(f'Question 19')
rows_of_twos = np.full((2, myArray5.shape[1]), 2)
myArray5 = np.vstack((myArray5, rows_of_twos))
print(myArray5)

print(f'Question 20')
myArray5 = myArray5[:, :-1]
print(myArray5)

print(f'Question 21')
myArray5 = myArray5[:-1, :]
print(myArray5)

print(f'Question 22')
myArray6 = np.array([[1, 2, 3], [4, 5, 6], [9, 8, 7]])
myArray6 = np.hstack((myArray6[:, :1], myArray6[:, 2:]))

print(myArray6)


print(f'Question 23')
exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
exercise_1[exercise_1 % 2 == 1] = -1

print(exercise_1)



print(f'Question 24')
exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
exercise_2_reshaped = exercise_2.reshape(3, -1)

print(exercise_2_reshaped)

print(f'Question 25')
exercise_3 = np.arange(4).reshape(2,-1)
print(exercise_3)
exercise_3 += 202
print(exercise_3)

print(f'Question 26')
random_integers = np.random.randint(30, 41, size=10)
print(random_integers)

print(f'Question 27')
x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])
more_than = np.where(x > y)
equal_= np.where(x == y)
print("Positions where x is more than y:", more_than)
print("Positions where x is equal to y:", equal_)

print(f'Question 28')
exercise_6 = np.arange(100).reshape(5, -1)
first_four_columns = exercise_6[:, :4]

print(first_four_columns)

