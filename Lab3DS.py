import pandas as pd
import numpy as np


print('Question 1')
# Test Data for the first DataFrame
data1 = {
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
    'marks': [200, 210, 190, 222, 199]
}
student_data1 = pd.DataFrame(data1)

#print(student_data1)

# Test Data for the second DataFrame
data2 = {
    'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
    'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
    'marks': [201, 200, 198, 219, 201]
}
student_data2 = pd.DataFrame(data2)
#print(student_data2)

# Joining the two dataframes along rows
combined_data = pd.concat([student_data1, student_data2], ignore_index=True)

print(combined_data)


print('Question 2')
data1 = {
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
    'marks': [200, 210, 190, 222, 199]
}
student_data1 = pd.DataFrame(data1)

#print(student_data1)

# Test Data for the second DataFrame
data2 = {
    'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
    'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
    'marks': [201, 200, 198, 219, 201]
}
student_data2 = pd.DataFrame(data2)
#print(student_data2)

# Joining the two dataframes along rows
combined_data = pd.concat([student_data1, student_data2], axis=1)

print(combined_data)



print('Question 3')
# New row(s) to append
new_rows = pd.DataFrame({
    'student_id': ['S6'],
    'name': ['Scarlette Fisher'],
    'marks': [205]
})

updated_student_data1_with_concat = pd.concat([student_data1, new_rows], ignore_index=True)

print(updated_student_data1_with_concat)

print('Question 4')
# List of dictionaries to append
new_data_dicts = [
    {'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 205}
]

# Appending the list of dictionaries to the existing DataFrame
updated_student_data1_with_dicts = pd.concat([student_data1, pd.DataFrame(new_data_dicts)], ignore_index=True)

print(updated_student_data1_with_dicts)

print('Question 5')
# Additional test data for exam_data
exam_data = {
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]
}
exam_data_df = pd.DataFrame(exam_data)

# Joining the two student dataframes along rows
combined_student_data = pd.concat([student_data1, student_data2], ignore_index=True)

# Merging combined student data with exam data on 'student_id'
merged_data = pd.merge(combined_student_data, exam_data_df, on='student_id', how='inner')

print(merged_data)

print('Question 6')
# Joining the two dataframes on the 'student_id' column using an inner join to get only the common entries
joined_data = pd.merge(student_data1, student_data2, on='student_id', how='inner', suffixes=('_1', '_2'))

print(joined_data)

print('Question 7')
# Joining the two dataframes on 'student_id' with matching records from both sides where available using an outer join
joined_data_outer = pd.merge(student_data1, student_data2, on='student_id', how='outer', suffixes=('_1', '_2'))

print(joined_data_outer)



print('Question 8')
# Test Data
data1 = {
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'P': ['P0', 'P1', 'P2', 'P3'],
    'Q': ['Q0', 'Q1', 'Q2', 'Q3']
}
df1 = pd.DataFrame(data1)

data2 = {
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'R': ['R0', 'R1', 'R2', 'R3'],
    'S': ['S0', 'S1', 'S2', 'S3']
}
df2 = pd.DataFrame(data2)

# Joining (left join) the two dataframes using keys from left dataframe only
joined_data_left = pd.merge(df1, df2, on=['key1', 'key2'], how='left')

print(joined_data_left)

print('Question 9')
# Joining (right join) the two dataframes using keys from right dataframe only
joined_data_right = pd.merge(df1, df2, on=['key1', 'key2'], how='right')

print(joined_data_right)

print('Question 10')
# Merging the two given datasets using multiple join keys (key1, key2)
merged_data_multiple_keys = pd.merge(df1, df2, on=['key1', 'key2'])

print(merged_data_multiple_keys)

print('Question 11')
# Creating sample Series
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series(['A', 'B', 'C', 'D', 'E'])

# Creating a new DataFrame from these series
new_df = pd.DataFrame({'Column1': series1, 'Column2': series2})

# Specifying new column names
new_df.columns = ['Number', 'Letter']

print(new_df)

print('Question 12')
# Identifying combinations of key1 and key2 that appear more than once in both dataframes
# Step 1: Merge dataframes to find common combinations
merged_common = pd.merge(df1, df2, on=['key1', 'key2'])

# Step 2: Find combinations appearing more than once in the merged dataframe
combinations_counts = merged_common.groupby(['key1', 'key2']).size()
combinations_more_than_once = combinations_counts[combinations_counts > 1].reset_index(name='Count')

# Step 3: Filter the merged_common dataframe to include only those combinations
result_df = merged_common.merge(combinations_more_than_once[['key1', 'key2']], on=['key1', 'key2'])

print(result_df)

print('Question 13')
data1 = {
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}
df1 = pd.DataFrame(data1, index=['K0', 'K1', 'K2'])

data2 = {
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
}
df2 = pd.DataFrame(data2, index=['K0', 'K2', 'K3'])

# Combining the columns of the two dataframes
combined_df = pd.concat([df1, df2], axis=1)

print(combined_df)

print('Question 14')
# Redefining test data for Task 14
data1 = {
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'P': ['P0', 'P1', 'P2', 'P3'],
    'Q': ['Q0', 'Q1', 'Q2', 'Q3']
}
df1_correct = pd.DataFrame(data1)

data2 = {
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'R': ['R0', 'R1', 'R2', 'R3'],
    'S': ['S0', 'S1', 'S2', 'S3']
}
df2_correct = pd.DataFrame(data2)

# Correctly merging the two given dataframes with different columns
merged_data_diff_columns_final = pd.merge(df1_correct, df2_correct, on=['key1', 'key2'], how='outer')

print(merged_data_diff_columns_final)


print('Question 15')
# Original DataFrames
df1 = pd.DataFrame({'A': [np.nan, 0.0, np.nan], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3.0, np.nan, 3.0]})

# Combining two DataFrame objects by filling null values in df1 with non-null values from df2
combined_df = df1.combine_first(df2)

print(combined_df)

