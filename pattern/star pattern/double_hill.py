n = 6

for i in range(1 , n + 1):
    print(" " * (n-i) , end="")
    print("* " * i , end="")
    print(" " * (n-i) * 2 , end="")
    print("* " * i)