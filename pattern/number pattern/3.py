n = 10
for i in range(1 , n + 1):
    print(" " * (n - i) , end="")
    for j in range(1 , i+1):
        if j % 2 == 0:
            print("0" ,end=" ")
        else:
            print("1" , end=" ")
    print()


n = 5
for i in range(1 , n + 1):
    print(" " * (n - i) , end="")
    for j in range(1 , i+1):
        print(j, end=" ")
    print()