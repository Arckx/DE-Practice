bonus = 5
tax = 10
salaries = {"Ahmed":80000, "Saad":90000, "Khizer": 150000}

emp = []
sal = []
bonus_salary = []
salary_tax = []

def list_employees(dict):
    for item,salary in dict.items():
        emp.append(item)
        sal.append(salary)

employees = list_employees(salaries)

def salary_bonus(sal, bonus):
    for salary in sal:
        bonus_cal = salary * bonus / 100
        bonus_salary.append(bonus_cal)

bonuses = salary_bonus(sal, bonus)

def tax_calculation(sal, tax):
    for salary in sal:
        tax_cal = salary * tax / 100
        salary_tax.append(tax_cal)
        
taxes = tax_calculation(sal, tax)

print(emp)
print(sal)
print(bonus_salary)
print(salary_tax)



net = []

def net_salary(salary, bonus, tax):
    result = 0
    for sal_x in salary:
        for bonus_x in bonus:
            for tax_x in tax:
                result = sal_x + bonus_x - tax_x
        net.append(result)

total = net_salary(sal, bonus_salary, salary_tax)

# print(net)

for key, value in zip(salaries.keys(), net):
    salaries[key] = value
print(salaries)