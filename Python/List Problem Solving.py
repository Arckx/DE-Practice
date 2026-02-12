# ## Beginner Level

# 1. **Reverse a list without using `reverse()`**
#    Input: `[1, 2, 3, 4]`
#    Output: `[4, 3, 2, 1]`

# x = [1, 2, 3, 4]
# y = []

# for i in -1, -2, -3, -4:
#     y.append(x[i])
# print(y)

# 2. **Find the maximum element in a list without using `max()`**
# x = [1, 2, 3, 4]
# val = x[0]
# for n in x:
#     if n > val:
#         val = n
# print(val)


# 3. **Count how many times a given number appears in a list**
# num = [1, 2, 3, 4, 4]
# count = 0
# target = 1
# for n in num:
#     if n == target:
#         count += 1
# print(count)


# 4. **Remove all occurrences of a given value from a list**
#    Input: `[1, 2, 3, 2, 4]`, remove `2`
#    Output: `[1, 3, 4]`

# num = [1, 2, 3, 2, 4]
# target = 2
# for n in num:
#     if n == target:
#         num.remove(n)
# print(num)

# 5. **Check if a list is sorted in ascending order**
# num = [1, 2, 3, 2, 4]

# for n in range(len(num) - 1):
#     if num[n] > num[n+1]:
#         print("Not Sorted")
#         break
#     else:
#         continue

# ## Intermediate Level

# 6. **Find the second largest number in a list (no sorting allowed)**
# num = [1, 2, 3, 5]
# high = 0
# second_high = 0
# for n in num:
#     if n > high:
#         second_high = high
#         high = n
#     elif n > second_high and n != high:
#         second_high = n
# print(high)
# print(second_high)

# 7. **Move all zeros to the end of the list while maintaining order**
#    Input: `[0, 1, 0, 3, 12]`
#    Output: `[1, 3, 12, 0, 0]`
# num = [0, 1, 0, 3, 12]
# result = []
# zero_count = 0

# for n in num:
#     if n == 0:
#         zero_count += 1
#     else:
#         result.append(n)

# for i in range(zero_count):
#     result.append(0)

# print(result)


# 8. **Find the intersection of two lists (common elements)**
#    Input: `[1, 2, 3]`, `[2, 3, 4]`
#    Output: `[2, 3]`
# j = [1, 2, 3]
# k = [2, 3, 4]
# l = []

# for x in j:
#     for y in k:
#         if x == y:
#             l.append(x)

# print(l)


# 9. **Remove duplicate elements from a list (preserve order)**
# num = [1, 2, 3, 2, 4]
# target = 2
# for i in range(len(num) - 1):
#     if num[i] == target:
#         num.remove(target)
# print(num)


# 10. **Split a list into two lists: even numbers and odd numbers**

# ## Advanced Level

# 11. **Rotate a list to the right by `k` steps**
#     Input: `[1, 2, 3, 4, 5]`, `k = 2`
#     Output: `[4, 5, 1, 2, 3]`

# 12. **Find all pairs of numbers whose sum is equal to a target**
#     Input: `[1, 2, 3, 4]`, target = `5`
#     Output: `[(1,4), (2,3)]`

# 13. **Flatten a nested list (1 level deep)**
#     Input: `[1, [2, 3], [4, 5]]`
#     Output: `[1, 2, 3, 4, 5]`

# 14. **Find the longest increasing continuous sublist**
#     Input: `[1, 2, 2, 3, 4, 1]`
#     Output: `[2, 3, 4]`

# 15. **Find the missing number in a list from 1 to N**
#     Input: `[1, 2, 4, 5]`
#     Output: `3`


# ## Data-Engineering Style Problems

# 16. **Chunk a list into fixed-size batches**
#     Input: `[1,2,3,4,5,6,7]`, size = `3`
#     Output: `[[1,2,3], [4,5,6], [7]]`

# 17. **Find the rolling average of a list with window size `k`**
#     Input: `[1, 2, 3, 4, 5]`, `k = 3`
#     Output: `[2.0, 3.0, 4.0]`

# 18. **Remove outliers: values greater than 2× the average**

# 19. **Merge two sorted lists into one sorted list (no sorting function)**

# 20. **Simulate deduplication in a data pipeline (keep first occurrence only)**
#     Input: `["A", "B", "A", "C", "B"]`
#     Output: `["A", "B", "C"]`
