n = 5

for i in range(n + 1):
    print(" " * (n - i) , end="")
    for j in range(i , -1 , -1):
        print(j , end="")
    for j in range(1 , i + 1):
        print(j , end="")
    print()