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


cand = [['Abdullah','Ahmed','AbdulRaheem'], [20, 30, 40]]

def person(name, age):
    print("my name is:", name, "I am", age ,"years old")


for i in range(3):
    person(cand[0][i], cand[1][i])

# print(cand[0][0], cand[1][0])












