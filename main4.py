import pandas as pd
import numpy as np
import os
print(os.getcwd())


df = pd.read_csv('titanic.csv')

print('Question 1')
print('')
print(df.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None))

print('Question 2')
print('')

print(df.columns)
print(df.shape)
print(df.dtypes)

print('Question 3')
print('')

#print(df.to_string())

pivot_table = df.pivot_table(values='survived', index=['sex', 'class'], aggfunc='mean')

print(pivot_table)

print('Question 4')
print('')


# Create a Pivot table to find survival rate by gender on various classes
pivot_table = pd.pivot_table(df, values='survived', index='sex', columns='pclass', aggfunc='mean')

# Print the Pivot table
print("Survival rate by gender on various classes:")
print(pivot_table)

print('Question 5')
print('')

pivot_table = df.groupby('sex')['survived'].mean().reset_index()

# Print the Pivot table
print("Survival rate by gender:")
print(pivot_table)

print('Question 6')
print('')

age_bins = [0, 18, 30, 50, 100]
age_labels = ['0-17', '18-29', '30-49', '50+']
df['ageGroup'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Create a Pivot table to find survival rate by gender, age wise of various classes
pivot_table = pd.pivot_table(df, index=['sex', 'ageGroup'], columns='pclass', values='survived', aggfunc='mean')

# Print the Pivot table
print("Survival rate by gender and age wise of various classes:")
print(pivot_table)

print('Question 7')
print('')

age_bins = [0, 10, 30, 60, 80]
age_labels = ['0-10', '10-30', '30-60', '60-80']

# Create a new column to assign passengers to age categories
df['ageCategory'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Display the DataFrame with the new AgeCategory column, omitting the Name column
print("Passengers partitioned into categories based on their age:")
print(df[['age', 'ageCategory']])

print('Question 8')
print('')
age_bins = [0, 10, 30, 60, 80]
age_labels = ['0-10', '10-30', '30-60', '60-80']

# Create a new column to assign passengers to age categories
df['AgeCategory'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Create a Pivot table to count survival by gender, categories wise age of various classes
pivot_table_survival = pd.pivot_table(df,
                                      index=['sex', 'ageCategory'],
                                      columns='pclass',
                                      values='survived',
                                      aggfunc='sum',
                                      fill_value=0)

# Display the Pivot table
print("Survival count by gender and age categories of various classes:")
print(pivot_table_survival)

print('Question 9')
print('')
age_bins = [0, 10, 30, 60, 80]
age_labels = ['0-10', '10-30', '30-60', '60-80']

# Create a new column to assign passengers to age categories
df['AgeCategory'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Create a Pivot table to count survival by gender, categories wise age of various classes
pivot_table_survival = pd.pivot_table(df,
                                      index=['sex', 'ageCategory'],
                                      columns='pclass',
                                      values='survived',
                                      aggfunc='mean'
)

# Display the Pivot table
print("Survival count by gender and age categories of various classes:")
print(pivot_table_survival)




print('Question 10')
print('')

data = {
    'survived': [1, 0, 1, 0, 0],
    'sex': ['male', 'female', 'female', 'male', 'male'],
    'age': [22, 38, 26, 35, 35],
    'fare': [7.25, 71.2833, 7.925, 53.1, 8.05],
    'pclass': [3, 1, 3, 1, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Assuming df is your DataFrame containing the data
fare = pd.qcut(df['fare'], 2)
age = pd.cut(df['age'], [0, 10, 30, 60, 80])
pivot_result = df.pivot_table('survived', index=['sex', age], columns=[fare, 'pclass'])

print(pivot_result)
