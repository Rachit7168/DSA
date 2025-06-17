#Regular
for i in range(1 , 6):
    print(" " * (6 - i) , end="")
    print("* " * i)

#Reverse
for i in range(6, -1 , -1):  # Step is -1
    print(" " * (6 - i), end="")  # Leading spaces
    print("* " * i)               # Stars
