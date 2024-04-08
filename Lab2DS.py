import pandas as pd
import numpy as np
print(f'Question 1')



data = [1, 2, 3, 4, 5,6]
series = pd.Series(data)

print(series)

print(f'Question 2')
data = [10, 20, 30, 40, 50]
series = pd.Series(data)


series_list = series.tolist()


print("List:", series_list)


print("Type:", type(series_list))

print(f'Question 3')
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

addition = series1 + series2

subtraction = series1 - series2

multiplication = series1 * series2

division = series1 / series2

print("Addition:\n", addition)
print("Subtraction:\n", subtraction)
print("Multiplication:\n", multiplication)
print("Division:\n", division)


print(f'Question 4')

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

equal = series1 == series2

greater_than = series1 > series2

less_than = series1 < series2

comparison_results = pd.DataFrame({
    'Equal': equal,
    'Greater than': greater_than,
    'Less than': less_than
})

print(comparison_results)


print(f'Question 5')
original_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

converted_series = pd.Series(original_dict)

print(converted_series)

print(f'Question 6')

numpy_array = np.array([10, 20, 30, 40, 50])


converted_series = pd.Series(numpy_array)


print(converted_series)
print(f'Question 7')

original_series = pd.Series([100, 200, 'python', 300.12, 400])

changed_series = pd.to_numeric(original_series, errors='coerce')

print(original_series)
print(changed_series)
print(f'Question 8')

original_df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
})


first_column_series = original_df['col1']


print(first_column_series)

print(type(first_column_series))

print(f'Question 9')
original_series = pd.Series([100, 200, 'python', 300.12, 400])

series_to_array = original_series.to_numpy()

print(series_to_array)

print(type(series_to_array))
print(f'Question 10')
sample_data = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}

df = pd.DataFrame(sample_data)

print(df)
print(f'Question 11')
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data, index=labels)

print(df)

print(f'Question 12')
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data, index=labels)

print("Summary of the basic information about this DataFrame and its data:")
df.info()

print(f'Question 13')
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data, index=labels)


first_three_rows = df.iloc[:3]

print("First three rows of the data frame:")
print(first_three_rows)
print(f'Question 14')
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data, index=labels)


selected_columns = df[['name', 'score']]


print("Select specific columns:")
print(selected_columns)
print(f'Question 15')
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data, index=labels)


selected_columns_rows = df.loc[['b', 'd', 'f', 'g'], ['name', 'score']]


print("Select specific columns and rows:")
print(selected_columns_rows)

print(f'Question 16')
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

output = df[df['attempts'] > 2]

print(output)

print(f'Question 17')
num_rows, num_columns = df.shape

print(num_rows, num_columns)

print(f'Question 18')
rows_with_nan_score = df[df['score'].isna()]

print(rows_with_nan_score)

print(f'Question 19')
rows_score_15_to_20 = df[df['score'].between(15, 20)]

print(rows_score_15_to_20)
