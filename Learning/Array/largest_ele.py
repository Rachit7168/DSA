num = [2 , 4 , 4 ,9 ,0 , 1 , 2 ,10 , 111 ,222]

largest = float("-inf")
s_largest = float("-inf")
for i in range(len(num)):
    if num[i] > largest:
        s_largest = largest
        largest = num[i]

print(largest)
print(s_largest)