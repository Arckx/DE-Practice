#Using List, Tuples, Sets, Dictionaries, Conditional Statements, Loops, Functions, and Error Logging.
#Create a program that contains all of the above in it.

import logging
logging.basicConfig(filename = 'activity_4th_may_2026.txt', level = logging.DEBUG, filemode='w', format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s")

logging.info("LOG Start")

list1 = []
list2 = []
dictionary = {'a': 1, 'b': 2, 'c': 3}

#Loops
logging.info("For Loop has started")
logging.info("Iterating over the dictionary items")
for key, value in dictionary.items():
    list1.append(key)
    list2.append(value)
logging.info("Added Keys and Values to separate lists as list1 and list2")

# Conditional Statements
# y = input("Enter a character ", )
try: 
    for i in range(5):
        x = int(input("Enter an integer ", ))
        list2.append(x)
except Exception as e:
        logging.debug("Faced an error, here it is ", e)
        print("Wrong Input", e)

print(list1)
print(list2)
#Functions
def addition(var):
    n = 0
    for i in var:
          n += i
    return n

if len(list2) > 3:
     print(addition(list2))

#Error Logging

logging.info("LOG END")