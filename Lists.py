#Create Lists

# empty = []
# letters = ['a', 'b', 'c']
# numbers = [1, 2, 3]
# mixed = [1, 'a', True, None]
# print(mixed)
# print(type(mixed))

#Builtin Functions

# empty = list()
# print(empty)

# letters = list('Python')
# print(letters)

# numbers = list(range(5))
# print(numbers)

#Create Nested List

# matrix = [['a', 'b', 'c'], 
#           ['d', 'e', 'f']]

# mixed_matrix = [['a', 'b'],
#                  [1, 2, 3],
#                  [True]]
# print(mixed_matrix)
# print(type(mixed_matrix))

#Access & Read

# lst = ['a', 'b', 'c', 'd']
# print(lst)
# #Slicing
# print(lst[:2])
# print(lst[2:])
# print(lst[:])

# matrix = [['a', 'b', 'c'], #Row 0
#           ['d', 'e', 'f'], #Row 1
#           ['g', 'h', 'i']] #Row 2

# print(matrix[2][:2])

#Unpacking Lists

# person = ['Maria', 29, 'Data Engineer', 'Spain']

# name, age, role, country = person
# print(role)

#Any Information that is not assigned a separate variable will be added to the asterisk variable

#Only one asterisk is allowed

# name, *details, country = person
# print(details)

#Underscore is used to trash info that is not needed to be extracted. 
#Can be used more than once
# name, _, role, _ = person
# print(name)

#Using both asterisk and underscore

# *_, country = person
# print(country)

#Making Changes to the List

#Adding items to the list

# letters = ['a', 'b', 'c']
# letters.append('x') #Adds at the end
# letters.append('y')

# letters.insert(1, 'f') #Adds where you specify the index
# letters.insert(3, 'y')
# print(letters)

# matrix = [['a', 'b', 'c'], #Row 0
#           ['d', 'e', 'f'], #Row 1
#           ['g', 'h', 'i']] #Row 2

# matrix[1].append('x')
# print(matrix)

#Remove items from the lists
# letters = ['a', 'b', 'c']
# letters.clear() #Empties whole list
# print(letters)

# letters = ['a', 'b', 'a']
# letters.remove('a') #Removes the first match
# print(letters)

# letters = ['a', 'b', 'c']
# removed = letters.pop(1) #Uses index for removing items, if empty it will remove the last item by default
# #It will also return the item that has been removed
# print(letters)
# print('Removed Item:', removed)

# matrix = [['a', 'b', 'c'], #Row 0
#           ['d', 'e', 'f'], #Row 1
#           ['g', 'h', 'i']] #Row 2

# # matrix.remove(['a', 'b', 'c'])
# # matrix.pop()
# matrix[1].remove('e')
# print(matrix)

#Update items in List

# letters = ['a', 'b', 'c']
# letters[0] = 'y' #This will update the list item specified with index
# letters[1] = 'x'
# letters = 'z' #This will update the whole list
# print(letters)

# matrix = [['a', 'b', 'c'], #Row 0
#           ['d', 'e', 'f'], #Row 1
#           ['g', 'h', 'i']] #Row 2

# matrix[-1] = ['x', 'y', 'z']
# matrix[0][0] = '-'
# matrix[1][1] = '-'
# matrix[-1][-1] = '-'
# print(matrix)

#Sorting Lists

# letters = ['c', 'a', 'b']
# letters.sort()
# # letters.sort(reverse = True)
# print(letters)

# matrix = [['d', 'e', 'f'],
#           ['a', 'z', 'i'],
#           ['a', 'a', 'c']]
# #Python sorts by comparing 1st letter of each item in list
# matrix[1].sort()
# print(matrix)

#Reverse List

# letters = ['c', 'a', 'b']
# new_list = list(reversed(letters))
# # letters.reverse()
# print('Original List', letters)
# print('Reversed List', new_list)



# a = [1, 2, 3, 4, 5, 6, 7]

# for i in range(a):
#     print(i)


# name = ['Ahmed', 'Abdullah', 'Abdur']

# print(len(name))

##############################
#List items of different types

# student = ['Jack', 32, 'Computer Science', [2, 4]]
# print(student)

#Access list elements
# languages = ['Python', 'Swift', 'C++']

# print('languages[0] =', languages[0])
# print('languages[1] =', languages[1])

#Negative Indexing

# languages = ['Python', 'Swift', 'C++']

# print('languages[-1] =', languages[-1])

#Slicing of a list
# my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

# print('my_list[2:5] =', my_list[2:5])
# print('my_list[2:-2] =', my_list[2:-2])

# #Omitting start and end indices in slicing
# print('my_list[5:] =', my_list[5:])
# print('my_list[:-4] =', my_list[:-4])

#Add elements to a pthon list
# fruits = ['apple', 'banana', 'orange']
# # print(fruits)

# # fruits.append('cherry')
# # print(fruits)

# #add elements at a specified index
# fruits.insert(2, 'mango')
# print(fruits)


#Add elements to a list from other iterables

# numbers = [1, 2, 3]
# print(numbers)

# even_numbers = [2, 4, 6]
# print(even_numbers)

# numbers.extend(even_numbers)
# print(numbers)

#Change list items
# colors = ['Red', 'Black', 'Green']
# print(colors)

# colors[0] = 'Purple'
# print(colors)

#Remove an item from the list
# numbers = [2, 4, 7, 9]
# numbers.remove(4)
# print(numbers)

#remove one or more elements from the list
# names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']
# #delete item at index 1
# # del names[1]
# # print(names)
# #delete items from 1 to 2 index
# del names[1:3]
# print(names)
# #delete entire list
# del names

#iterting through a list
# fruits = ['apple', 'banana', 'orange']
# for fruit in fruits:
#     print(fruit)
