# def clean_name(first_name, last_name, country):
#     first = first_name.strip().lower()
#     last = last_name.strip().lower()
#     full_name = first + " " + last
#     print(full_name, "From", country)

# #Positional Arguments (if 2-3)
# clean_name("MarIA", "SMITH", "DE") 
# #Keyword Arguments (if >3)
# clean_name(first_name = "MarIA", last_name = "SMITH", country = "DE")



# name = 'abdullah'
# age = 26
# address = 'Haripur'

# def candidate(c_name,c_age,c_address):
#     print(c_name)
#     print(c_age)
#     print(c_address)


# inf = candidate(name,age,address)



# def sum(a,b):
#     c = a+b
#     return c

# summing = sum(a=5,b=5)
# div = summing / 5
# print(div)


# cand = [['Abdullah','Ahmed','AbdulRaheem'], [20, 30, 40]]

# def person(name, age):
#     print("my name is:", name, "I am", age ,"years old")


# for i in range(3):
#     person(cand[0][i], cand[1][i])

# print(cand[0][0], cand[1][0])


#Practicing Function

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")

# greet("Ahmed", "Rustam")

# def get_greeting(name):
#     return f"Hi {name}"

# message = get_greeting("Ahmed")

#Positional Arguments
# def increment(number, by):
#     return number + by

# print(increment(2, 1))

#Default Arguments
#default parameters should be at the end, means the requirement parameters will be written first in the function.
# def increment(number, by=1): #by is set as default
#     return number + by

# print(increment(1, 6))

# # *args
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2, 3, 4, 5))

# # **args
# def save_user(**user):
#     print(user) #prints dictionary

# save_user(id= 1, name= "John", age=22)


#Generate a Python list of all the even numbers between 4 to 30

# def even_number():
#     list = []
#     for num in range(4, 30):
#         if num%2 == 0:
#             list.append(num)
#     return list

# print(even_number())

#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 

# x = int(input("Enter the number to perform the factorial: "))

# def factorial(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result

# print(f"Factorial of {x} is: ", factorial(x))

bonus = 5
tax = 10
salaries = {"Ahmed":80000, "Saad":90000, "Khizer": 150000}

def list_employees(dict):
    emp = []
    sal = []
    for item,salary in dict:
        emp.append(item)
        sal.append(salary)

    return emp

employees = list_employees(salaries)

def extract_salary(sal):
    salary_list = []
    for person in sal:
        salary_list.append(sal[person])
    return salary_list

salary_list = extract_salary(salaries)

def salary_bonus(sal, bonus):
    bonus_salary = []
    for salary in sal:
        bonus_cal = salary * bonus / 100
        salary += bonus_cal
        bonus_salary.append(bonus_cal)
        bonus_salary.append(salary)
    return bonus_salary
    
bonus_list = salary_bonus(salary_list, bonus)

def tax_calculation(sal, tax):
    salary_tax = []
    for salary in sal:
        tax_cal = salary * tax / 100
        salary -= tax_cal
        salary_tax.append(tax_cal)
        salary_tax.append(salary)
    return salary_tax

tax_deduct = tax_calculation(salary_list, tax)

def net_salary(salary, bonus, tax):
    net_salary = 0
    for sal in salary:
        net_salary += sal
        print(net_salary)
    for sal_bonus in bonus:
        net_salary += sal_bonus
    for sal_tax in tax:
        net_salary -= sal_tax
    return net_salary

print(net_salary(salary_list, bonus_list, tax_deduct))