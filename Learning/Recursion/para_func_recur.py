# ----------------------------------------
# Q4: Sum of Numbers from 1 to N using Recursion
# ----------------------------------------

# Parameterized Recursion (Passing sum as a parameter)
def sum_1_to_n_parameterized(i, n, sum=0):
    if i > n:
        print(sum)
        return
    sum_1_to_n_parameterized(i + 1, n, sum + i)

# Functional Recursion (Return value used in recursive expression)
def sum_1_to_n_functional(n):
    if n == 1:
        return 1
    return n + sum_1_to_n_functional(n - 1)

# ----------------------------------------
# Function Calls (Test them one by one)
# ----------------------------------------

# Q4:
# sum_1_to_n_parameterized(1, 5)       # Output: 15
# print(sum_1_to_n_functional(5))      # Output: 15