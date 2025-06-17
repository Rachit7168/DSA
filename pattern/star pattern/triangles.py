for i in range(1 , 6):
    print("*" * i)
for i in range(6 , -1 , -1 ):
    print("*" * i)

for i in range(1 , 6):
    print(" " * (6 - i) , end="")
    print("*" * i )
for i in range(6 , -1 , -1 ):
    print(" " * (6 - i) , end="")
    print("*" * i )


