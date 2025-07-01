name = "Rachit"

for i in range(1 , len(name) + 1):
    print(name[:i])
    
arr = [9 , 3 , 2, 1]
maxi = arr[0]
for num in arr:
    if num > maxi:
        maxi = num
print(maxi)

mini = arr[0]
for num in arr:
    if num < mini:
        mini = num
print(mini)

arr = [1 ,2, 3 , 1 , 2, 3]
seen = []
for num in arr:
    if num not in seen:
        seen.append(num)
    arr = seen
print(arr)