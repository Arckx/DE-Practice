# ### **Challenge 1: Common Users**

# **Input:**
# Two lists of user IDs

# ```python
# system_a = [1, 2, 3, 4]
# system_b = [3, 4, 5, 6]
# ```

# **Task:**
# Return a set of users present in **both systems**.

# **Hint:** Use set intersection.

# ---

# ### **Challenge 2: Unique Emails**

# **Input:**

# ```python
# emails = ["a@mail.com", "b@mail.com", "a@mail.com"]
# ```

# **Task:**
# Return a set of **unique email addresses**.

# **Hint:** Convert list → set.

# ---

# ### **Challenge 3: Users Who Didn’t Login**

# **Input:**

# ```python
# all_users = {1, 2, 3, 4, 5}
# logged_in_today = {2, 4}
# ```

# **Task:**
# Return users who **did not log in today**.

# **Hint:** Set difference.

# ---

# ### **Challenge 4: Exclusive Department Employees**

# **Input:**

# ```python
# dept_a = {101, 102, 103}
# dept_b = {103, 104, 105}
# ```

# **Task:**
# Return employees who are in **only one department**.

# **Hint:** Symmetric difference.

# ---

# ### **Challenge 5: Same Products Check**

# **Input:**

# ```python
# warehouse_1 = {1, 2, 3}
# warehouse_2 = {3, 2, 1}
# ```

# **Task:**
# Return `True` if both warehouses store **exactly the same products**.

# **Hint:** Direct set comparison.

# ---

# ### **Challenge 6: Detect Duplicates**

# **Input:**

# ```python
# numbers = [1, 2, 3, 4, 2]
# ```

# **Task:**
# Return `True` if duplicates exist, else `False`.

# **Hint:** Compare length of list vs set.

# ---

# ### **Challenge 7: Banned IP Check**

# **Input:**

# ```python
# banned_ips = {"192.168.1.1", "10.0.0.1"}
# ip = "192.168.1.1"
# ```

# **Task:**
# Check whether the IP is banned.

# **Hint:** Membership test in set.

# ---

# ### **Challenge 8: Invalid File Types**

# **Input:**

# ```python
# allowed = {"jpg", "png", "pdf"}
# uploaded = {"jpg", "exe", "pdf"}
# ```

# **Task:**
# Return invalid file extensions.

# **Hint:** Difference between sets.

# ---

# ### **Challenge 9: Unique Word Count**

# **Input:**

# ```python
# sentence = "data engineering is data driven"
# ```

# **Task:**
# Return the **count of unique words**.

# **Hint:** `split()` then set.

# ---

# ### **Challenge 10: Tasks Done by Both Teams**

# **Input:**

# ```python
# team_a = {1, 2, 3}
# team_b = {3, 4, 5}
# ```

# **Task:**
# Return tasks completed by **both teams**.

# **Hint:** Intersection.

# ---

# ### **Challenge 11: Safe Removal**

# **Input:**

# ```python
# active_users = {"u1", "u2", "u3"}
# user_to_remove = "u4"
# ```

# **Task:**
# Remove the user **without raising an error**.

# **Hint:** `discard()` instead of `remove()`.

# ---

# ### **Challenge 12: Permission Check**

# **Input:**

# ```python
# user_permissions = {"read", "write"}
# required_permissions = {"read"}
# ```

# **Task:**
# Return `True` if user has all required permissions.

# **Hint:** Subset check.

# ---

# ### **Challenge 13: Unpaid Customers**

# **Input:**

# ```python
# orders = {1, 2, 3, 4}
# payments = {2, 4}
# ```

# **Task:**
# Return customers who placed orders but didn’t pay.

# **Hint:** Set difference.

# ---

# ### **Challenge 14: All Unique Tags**

# **Input:**

# ```python
# tags_1 = {"python", "data"}
# tags_2 = {"sql", "data"}
# tags_3 = {"etl", "python"}
# ```

# **Task:**
# Return all unique tags.

# **Hint:** Union of multiple sets.

# ---

# ### **Challenge 15: No Common Elements**

# **Input:**

# ```python
# a = {1, 2, 3}
# b = {4, 5, 6}
# ```

# **Task:**
# Return `True` if sets share **no common elements**.

# **Hint:** `isdisjoint()`.

# ---

# ### **Challenge 16: Process Only Once**

# **Input:**

# ```python
# stream = [1, 2, 2, 3, 4, 4]
# ```

# **Task:**
# Return values that should be processed **once**.

# **Hint:** Use a set to track seen values.



# ### **Challenge 17: Remove Common Elements**

# **Input:**

# ```python
# main_set = {1, 2, 3, 4}
# remove_set = {3, 4}
# ```

# **Task:**
# Modify `main_set` to remove shared elements.

# **Hint:** In-place set operation.



# ### **Challenge 18: Course Completion**

# **Input:**

# ```python
# required = {"math", "cs", "db"}
# completed = {"math", "cs", "db", "ai"}
# ```

# **Task:**
# Check if all required courses are completed.

# **Hint:** Subset logic.



# ### **Challenge 19: Appears Only Once**

# **Input:**

# ```python
# nums = [1, 2, 2, 3, 4, 4, 5]
# ```

# **Task:**
# Return numbers that appear **only once**.

# **Hint:** Use set math between original and duplicates.



# ### **Challenge 20: Sorted Output**

# **Input:**

# ```python
# values = {5, 1, 3, 2, 4}
# ```

# **Task:**
# Return a **sorted list** of values.

# **Hint:** Convert set → list → sort.


