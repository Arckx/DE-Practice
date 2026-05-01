# my_dict = {
#     'a': 10,
#     'b': 20,
#     'c': 30
# }
# print(my_dict)

# user = {"id": 1, "age": 30, "city": "berlin"}

#Access
# # print(user["name"])
# print(user.get('name', "Unknown"))

# #Checks
# print("age" in user)
# print("name" not in user)

# #View Objects
# print(user.keys())
# print(user.values())
# print(user.items()) #List of tuples
# print(user)

# #Looping
# for u in user:
#     print(u, user[u])

# for key, value in user.items():
#     print(key, value)

# #Add, Remove, Update
# user["name"] = "John" #Add
# user["age"] = 35 #Update
# user.update({"age": 40, "city": "Paris"}) #Multi Update
# user.pop("age") #Remove
# user.popitem() #Returns & Deletes most recent key value pair
# print(user)

#Creation
# user = {"id": None,
#         "name": None,
#         "age": None,
#         "city": None  
#     } This way of creating dictopnary is not good, if you dont have the values.

# user = dict.fromkeys(["id", "name", "age", "city"], None)
# print(user)

#Challenge
# user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

# user_str = {
#     k: v.upper()
#     for k, v in user.items()
#     if isinstance(v, str)
# }

# print(user_str)

#Nested Dictionary
people = {
    1: {'name': 'John', 'age': '27', 'gender': 'Male'},
    2: {'name': 'Marie', 'age': '22', 'gender': 'Female'}
}

#Accessing elements of a nested dictionary
# print(people[2]['name'])
# print(people[2]['age'])
# print(people[2]['gender'])

#Add elements to a nested dictionary
people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['gender'] = 'Female'
people[3]['married'] = 'No'

# print(people[3])

#Add another dictionary to a nested dictionary
people[4] = {'name': 'Peter', 'age': '29', 'gender': 'Male', 'married': 'Yes'}
# print(people[4])

#Delete elements from the nested dictionary
# del people[3]['married']
# del people[4]['married']

# print(people[3])
# print(people[4])

#Delete dictionary from nested dictinary
# del people[3], people[4]
# print(people)

#Iterating through Nested dictionary
for p_id, p_info in people.items():
    print("\nPerson ID: ", p_id)

    for key in p_info:
        print(key + ':', p_info[key])
