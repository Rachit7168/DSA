n = 5

# Upper Half
for i in range(1, n + 1):
    # Left wing (>)
    print("*" * i, end="")

    # Spaces between wings
    print(" " * (2 * (n - i)), end="")

    # Right wing (<)
    print("*" * i)

# Lower Half
for i in range(n - 1, 0, -1):
    # Left wing (>)
    print("*" * i, end="")

    # Spaces between wings
    print(" " * (2 * (n - i)), end="")

    # Right wing (<)
    print("*" * i)
