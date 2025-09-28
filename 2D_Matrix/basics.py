matrix = [[5,2,3],[7,6,3],[2,3,9]]

rows = len(matrix)
cols = len(matrix[0])

result = [[0] * rows for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        result[j][i] = matrix[i][j]
print(result)

for i in range(rows):
    for j in range(cols):
        if j >= i:
            print(matrix[i][j] , end=" ")
        else:
            print("*" , end=" ")
    print()
    
for i in range(rows):
    for j in range(cols):
        if j <= i:
            print(matrix[i][j] , end=" ")
        else:
            print("*" , end=" ")
    print()
    
for i in range(rows):
    for j in range(cols):
        if j == i:
            print(matrix[i][j] , end=" ")
        else:
            print("*" , end=" ")
    print()
    
for i in range(rows):
    for j in range(cols):
        if j + i == rows - 1:
            print(matrix[i][j] , end=" ")
        else:
            print("*" , end=" ")
    print()