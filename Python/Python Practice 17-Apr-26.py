# Write a program that takes a number and prints whether it is even or odd.
# n = int(input("Enter the number: "))
# if n%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# Print numbers from 1 to 50, but:

# If divisible by 3 → print "Fizz"
# If divisible by 5 → print "Buzz"
# If both → "FizzBuzz"
# for i in range(1, 50):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Create a function that takes a list of numbers and returns the maximum number.
# n = [1,2,3,40,5,6,7,8,35,9]
# def max_num(num):
#     high_num = 0
#     for i in num:
#         if high_num < i:
#             high_num = i
#     print(high_num)
# max_num(n)

# Split your program into two files:

# One file has a function to calculate square of a number
# Second file imports and uses it

# import mymodule
# mymodule.square(5)

# Problem:
# Remove duplicates from a list.

# n = [1,1,2,7,5,8,9,4,4]
# m = set(n)
# print(m)

# Problem:
# Count frequency of each word in a sentence.

sentence = "data engineering is fun and data engineering is powerful and data is everywhere"

words = sentence.lower().split(" ")
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)

