#General way of using for loop on lists
# order_amounts = [100, 200, 50, 500, 400, 900, 1200, 70]
# orders_including_gst = []
# for x in order_amounts:
#     orders_including_gst.append(x+x*.18)
# print(orders_including_gst)

#List Comprehension
#Example 1
# order_amounts = [100, 200, 50, 500, 400, 900, 1200, 70]
# orders_including_gst = [x+x*.18 for x in order_amounts]
# print(orders_including_gst)

#Example 2
# order_amounts = [(100,5), (200,18), (50,12), (500,18), (400,12), (900,5), (1200,18), (70,12)]
# # orders_including_gst = []
# # for x in order_amounts:
# #     orders_including_gst.append(x[0] + x[0]*x[1]/100)
# # print(orders_including_gst) 

# orders_including_gst = [(x[0], x[1], x[0] + x[0]*x[1]/100) for x in order_amounts]
# print(orders_including_gst)

#Example 3 (Nested List)
#Output = [[1,1,1], [2,4,8], [3,9,27]]
# nested_lists = []
# for i in range(1,4):
#     nested_lists.append([i, i**2, i**3])
# print(nested_lists)

# nested_lists = [[i, i**2, i**3] for i in range(1,4)]
# print(nested_lists)

# # flattened_list = []
# # for sublist in nested_lists:
# #     for item in sublist:
# #         flattened_list.append(item)
# # print(flattened_list)

# flattened_list = [item for sublist in nested_lists for item in sublist]
# print(flattened_list)

#Example 4 
# orders_list = [
#     [101, '2023-07-25 00:00:00.0', 11599, 'CLOSED'],
#     [102, '2023-07-25 00:00:00.0', 256, 'PENDING_PAYMENT'],
#     [103, '2023-07-25 00:00:00.0', 12111, 'COMPLETE']
# ]
# closed_orders = [order for order in orders_list if order[3] == 'CLOSED']
# print(closed_orders)

#Unpacking (same way of unpacking the tuples)
# orders = [101, '2023-07-25 00:00:00.0', 11599, 'CLOSED']
# # order_id,order_date,customer_id,order_status = orders
# # print(order_id,order_date,customer_id,order_status)
# for index, element in enumerate(orders):
#     print(f'Index: {index}, Element: {element}')


#Example 5
#count the number of occurences of each word
# input_list = ["hello", "HELLO", "I", "AM", "AM", "sumit", "sumit"]
# input = input("Enter the text: ")
# input_list = input.split(" ")
# input_list_lower = [word.lower() for word in input_list]
# input_set = set(input_list_lower)
# # print(input_set)
# result_list = []
# for word in input_set:
#     result_list.append((word, input_list_lower.count(word)))
# print(result_list)


#Example 6
#count the number of order statuses
# data = """order_id,order_date,order_customer_id,order_status
# 1,2013-07-25 00:00:00.0,1159,CLOSED
# 2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT
# 3,2013-07-25 00:00:00.0,12111,COMPLETE
# 4,2013-07-25 00:00:00.0,8827,CLOSED
# 5,2013-07-25 00:00:00.0,11318,COMPLETE
# 6,2013-07-25 00:00:00.0,7130,COMPLETE
# 7,2013-07-25 00:00:00.0,4530,COMPLETE
# 8,2013-07-25 00:00:00.0,2911,PROCESSING
# 9,2013-07-25 00:00:00.0,5657,PENDING_PAYMENT
# 10,2013-07-25 00:00:00.0,5648,PENDING_PAYMENT"""

# lines = data.split("\n")[1:]
# lines_tuple = [tuple(line.split(",")) for line in lines]
# status_list = [line[3] for line in lines_tuple]

# #Assignment 1: Find the count of each order status
# status_set = set(status_list)
# words_count = []
# for words in status_set:
#     words_count.append((words, status_list.count(words)))
# print(words_count)

#Assignment 2: Find the count of each status
# list = [ [1, 100, 'success'],
#         [2, 200, 'pending'],
#         [3, 150, 'success'],
#         [4, 300, 'failed'],
#         [5, 400, 'success'],
#         [6, 250, 'pending'],
#         [7, 350, 'failed'],
#         [8, 450, 'success'],
#         [9, 500, 'pending'],
#         [10, 600, 'failed']
# ]

# status_list = [(item[2]) for item in list]
# status_set = set(status_list)
# words_count = [(status, status_list.count(status)) for status in status_set]
# print(words_count)

#Assignment 4: find the average salary for each department

emp_salary = [
    [101, 'John', 'IT', 60000],
    [102, 'Alice', 'HR', 50000],
    [103, 'Bob', 'Finance', 70000],
    [104, 'Emma', 'IT', 55000],
    [105, 'David', 'Finance', 75000],
    [106, 'Sophia', 'HR', 48000]
]

# dept_salary = [[salary[2], salary[3]] for salary in emp_salary]
# dept_list = [dept[0] for dept in dept_salary]
# dept_set = set(dept_list)
# count_dept = [[dept, dept_list.count(dept)] for dept in dept_set]
# # count_dept.sort()
# dept_dict = {}
# for key,value in dept_salary:
#     dept_dict[key] = dept_dict.get(key,0) + value
# total_salary = list(dept_dict.items())
# total_salary.sort()
# # print(total_salary)
# avg_dept_salary = []

# for salary in total_salary:
#     for department in salary:
#         dept_id = salary[0]
#         # print(dept_id)
#         sal = salary[1]
#         # print(sal)
#         for dept in count_dept:
#             for count in dept:
#                 # print(count)
#                 if count == dept_id:
#                     # print(count[1])
#                     count = dept[1]
#                     avg = salary / count
#                     avg_dept_salary.append((dept_id, avg))

# # print(avg_dept_salary)

dept = [line[2] for line in emp_salary]
unique=set(dept)
avg_sal=[(dt,sum(line[3] for line in emp_salary if line[2]==dt),sum(line[3] for line in emp_salary if line[2]==dt)/dept.count(dt)) for dt in unique]
print(avg_sal)