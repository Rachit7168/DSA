# ----------------------------------------
# Q5: Factorial of a Number using Recursion
# ----------------------------------------

# Functional Recursion (Return value used in recursive expression)
def factorial(n):
    if n is not int :
        return TypeError
    if n == 1:
        return 1
    return n * factorial(n - 1)

# ----------------------------------------
# Function Call (Test it here)
# ----------------------------------------

# Q5:
print(factorial("abc"))       # Output: 5040
