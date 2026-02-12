#List, Tuples, Sets, Dictionary, Sets, If-else, try-except, loops and functions.

# Sum of Even Numbers in a List
# Problem: Write a function that takes a list of numbers and returns the sum of all even numbers.

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def even_number(x):
#     z = 0
#     for i in x:
#         if i%2 == 0:
#             z += i
#     print(z)

# even_number(num)

# Find the Largest and Smallest in a List
# Problem: Create a function that returns both the largest and smallest numbers from a list.

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def comparison(x):
#     print("This is the largest number: ", max(x))
#     print("This is the smallest number: ", min(x))

# comparison(num)

# Frequency Counter
# Problem: Write a function that takes a string and returns a dictionary with the frequency of each character.

# word = "Hello"

# def counter(x):
#     z = {}
#     for i in x:
#         if i in z:
#             z[i] += 1
#         else:
#             z[i] = 1
#     return(z)


# print(counter(word))


# Merge Two Dictionaries
# Problem: Write a function to merge two dictionaries into one. If keys overlap, sum their values.

# dict1 = {'apple': 10, 'banana': 5, 'orange': 8}
# dict2 = {'banana': 7, 'orange': 3, 'grape': 6}

# def merger(d1, d2):
#     merged = d1
#     for key, value in d2.items():
#         if key in merged:
#             merged[key] += value
#         else:
#             merged[key] = value
#     print(merged)
# merger(dict1, dict2)
# print(dict1)

# Find Key with Maximum Value
# Problem: Write a function that finds the key with the highest value in a dictionary.

# dict1 = {'apple': 10, 'banana': 5, 'orange': 8}

# def high(x):
#     z = max(x, key = x.get)
#     print(z)

# high(dict1)

# Shopping Cart Total
# Problem: Write a function that takes a dictionary representing a shopping cart (item: price) and a list of items to buy. Return the total cost of items in the list.

cart = {
    "apple": 120,
    "banana": 60,
    "milk": 250,
    "bread": 180,
    "eggs": 300,
    "butter": 450
}

items_to_buy = ["milk", "apple", "eggs", "banana", "cheese"]

def checkout(items_cart, items_buying):
    total = 0
    for key, value in items_cart.items():
            for bought in items_buying:
                  if bought == key:
                    total += value
                    print(bought, value)
    print("Total:", total)       

checkout(cart, items_to_buy)
