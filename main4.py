import pandas as pd

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

print(df.to_string())

pivot_table = df.pivot_table(values='survived', index=['sex', 'class'], aggfunc='mean')

print(pivot_table)

print('Question 4')
print('')