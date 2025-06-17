# Bubble Sort

array = [5, 3, 8, 6, 2, 4]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
    return arr

print(bubble_sort(array))

#Selection Sort

array = [5, 3, 8, 6, 2, 4]
# index  0  1  2  3  4  5
# TODO : iteration one(i = 0)
# outer Loop
# smallestidx = arr[i] -> arr[o] = 5
# Inner loop
# i + 1 = 0 + 1 = 1 end at 6 (1 , 6)
# arr[j] < arr[smallestidx] -> arr[1] , arr[0] -> 3 < 5
# True So, smallestndx = j -> 1
# arr[j] < arr[smallestidx] -> arr[2] , arr[1] -> 8 < 3
# arr[j] < arr[smallestidx] -> arr[3] , arr[1] -> 6 < 3
# arr[j] < arr[smallestidx] -> arr[4] , arr[1] -> 2 < 3
# True So , smallestidx = j -> 4
# arr[j] < arr[smallestidx] -> arr[5] , arr[4] -> 4 < 2

def selection_sort(arr): # i = 0 - > smallest
    for i in range(len(arr)):
        smallestidx = i
        for j in range(i + 1 , len(arr)):
            if arr[j] < arr[smallestidx]:
                smallestidx = j
        arr[i] , arr[smallestidx] = arr[smallestidx] , arr[i]
    return arr

print(selection_sort(array))