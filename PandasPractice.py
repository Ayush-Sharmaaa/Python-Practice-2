import pandas as pd

series_list = pd.Series([1, 2, 3])
print("Pandas series from a list: ", series_list)
series_dict = pd.Series({'a': 10, 'b': 20})
print("Pandas series from a dictionary: ", series_dict)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Shivangi', 'Rahul', 'Priyanshi', 'Rohan'],
    'Age': [25, 32, 28, 29, 30, 31, 35],
    'Salary': [50000, 60000, 55000, 58000, 60000, 49000, 50000],
}
df = pd.DataFrame(data)
print("This is a DataFrame: \n", df)

df = pd.read_csv('file.csv') 
print("This is our simple csv: ", df)


print("These are the first 5 rows of the DataFrame: \n", df.head(5))
print("These are the last 5 rows of the DataFrame: \n", df.tail(5))

# Add column
df['Department'] = ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR']
print("After adding a new column as Department: ", df)


age_filter = df[df['Age'] > 30]
print("Rows with age greater than 30: \n", age_filter)

above_avg = df[df['Salary'] > df['Salary'].mean()]
print("Rows with salary greater than average: \n", above_avg)

df.rename(columns={'Salary': 'Income'}, inplace=True) #Here we committed the change in original dataframe.
print("After changing salary colum to income: \n", df)

print("Selecting specific columns: \n", df[['Name', 'Income']]) #Selecting specific column: Name and salary

grouped_avg = df.groupby('Department')['Income'].mean()
print("After grouping by department and calculating average income: ", grouped_avg)

sorted_df = df.sort_values(by='Age', ascending=False)
print("Sorted the dataframe by age in descending order: \n", sorted_df)

df.drop('Age', axis=1, inplace=True)
print("After removing age column: \n", df)

count_dept = df['Department'].value_counts()
print("Number of employees in each department: \n", count_dept)

max_salary = df.groupby('Department')['Income'].max()
print("Maximum salary in each department: ", max_salary)

df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['A', 'B']})
print("DataFrame1 is: ", df1)
df2 = pd.DataFrame({'ID': [1, 2], 'Marks': [80, 90]})
print("DataFrame2 is: ", df2)
merged = pd.merge(df1, df2, on='ID')
print("After merging both dataframes: \n", merged)