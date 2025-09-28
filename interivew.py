# Pattern
n = 5 
for i in range(1 , n + 1):
    print(" " * (n -i) , end="")
    for j in range(1 , i + 1):
        print(j , end="")
    for j in range(i - 1 , 0 , -1):
        print(j , end="")
    print()

# Array 
arr = [0, 1, 0, 3, 12]

i = 0
j = i + 1

while j < len(arr):
    if arr[i] == 0 and arr[j] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    j += 1

print(arr)


n = 5

# (10n -1 / 9) ** 2


for i in range(1 , n + 1):
    num = (10 ** i - 1) // 9
    square = num ** 2
    print(" " * (n - i) , end="")
    print(square)

n = 5

for i in range(1 , n + 1):
    nums = 2 * i - 1
    print(" " * (n - i) , end="")
    for j in range(nums , 0 , -1):
        print(j ,end="")
    print()