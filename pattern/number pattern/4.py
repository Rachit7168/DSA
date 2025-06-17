# n = 5 
# for i in range(1 , n + 1):
#     for j in range(1 , i + 1):
#         print(i , end=" ")
#     print()

# n = 5 
# for i in range(1 , n + 1):
#     for j in range(1 , i + 1):
#         print(n - i + 1, end=" ")
#     print()

# n = 5 
# p = 0
# for i in range(1 , n + 1):
#     for j in range(1 , i + 1):
#         print(p , end=" ")
#     p += 2
#     print()

# n = 5 
# for i in range(1 , n + 1):
#     for j in range(1 , i + 1):
#         if i % 2 == 0 :
#             print("2 " , end="")
#         else:
#             print("1 " , end="")
#     print()

n = 5 
p = 1
for i in range(1 , n + 1):
    print(" " * (n - i) , end="")
    for j in range(1 , i + 1):
        print(p ,  end=" ")
    p += 1
    print()

for i in range(n - 1 , -1 , -1):
    print(" " * (n - i) , end="")
    for j in range(1 , i + 1):
        print(p ,  end=" ")
    p += 1
    print()
