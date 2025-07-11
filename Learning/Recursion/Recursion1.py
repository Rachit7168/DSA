# ----------------------------------------
# Q1: Print x, n times using Recursion
# ----------------------------------------

# Tail Recursion (Print before recursive call)
def print_x_tail(x, n):
    if n == 0:
        return
    print(x)
    print_x_tail(x, n - 1)

# Head Recursion (Print after recursive call)
def print_x_head(x, n):
    if n == 0:
        return
    print_x_head(x, n - 1)
    print(x)

# ----------------------------------------
# Q2: Print 1 to N
# ----------------------------------------

# Tail Recursion (Print before recursive call)
def print_1_to_n_tail(i, n):
    if i > n:
        return
    print(i)
    print_1_to_n_tail(i + 1, n)

# Head Recursion (Print after recursive call)
def print_1_to_n_head(i, n):
    if i > n:
        return
    print_1_to_n_head(i + 1, n)
    print(i)

# ----------------------------------------
# Q3: Print N to 1 (Reverse Order)
# ----------------------------------------

# Simple Tail Recursion (Decrement n each time)
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)

# Head Recursion (Go up to N, then print from N to 1)
def print_n_to_1_head(i, n):
    if i > n:
        return
    print_n_to_1_head(i + 1, n)
    print(i)

# ----------------------------------------
# Function Calls (You can test them one by one)
# ----------------------------------------

# Q1:
# print_x_tail("Rachit", 3)       # Output: Rachit Rachit Rachit
# print_x_head("Rachit", 3)       # Output: Rachit Rachit Rachit (in reverse order of call stack)

# Q2:
# print_1_to_n_tail(1, 4)         # Output: 1 2 3 4
# print_1_to_n_head(1, 4)         # Output: 4 3 2 1

# Q3:
# print_n_to_1(4)                 # Output: 4 3 2 1
# print_n_to_1_head(1, 4)         # Output: 4 3 2 1
