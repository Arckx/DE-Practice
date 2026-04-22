import pandas as pd

#Load CSV
employees = pd.read_csv("employees_raw.csv")

#Data Tye Casting
employees = employees.astype({'age': int, 'salary': int, 'joining_date': 'datetime64[ms]'})

#Add new columns
employees['salary_after_tax'] = employees['salary'] - (employees['salary'] * 0.10)

employees['experience_years'] = 2026 - employees['joining_date'].dt.year

# #Remove a column
# employees.drop(columns=['city'], inplace=True)

# #Insert a row
employees.loc[len(employees)] = {'emp_id':9, 'name': 'Bilal', 'age': 29, 'department': 'IT', 'salary': 65000, 'joining_date': '2024-02-01', 'city': 'Lahore'}

#Filtering Transfoormation
print(employees[(employees['salary'] > 55000) & ((employees['department'] == 'IT') | (employees['department'] == 'Finance'))])

#Saving the CSV
employees.to_csv("employees_transformed.csv", index=False)