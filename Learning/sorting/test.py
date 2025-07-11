nums = [5, 7, 8, 4, 1, 6, 9, 2]

def selection_sort(arr):
    n = len(arr)
    for i in range(0 , n):
        min_index = i
        for j in range(i + 1 , n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    return arr

SELECTION_SORT = selection_sort(arr=nums)
print( "Selection Sort : " , SELECTION_SORT)

def bubble_srot(arr):
    n = len(arr)
    for i in range(n - 2 , -1 , -1):
        is_swaped = False
        for j in range(0 , i + 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
                is_swaped = True
        if is_swaped == False :
            break
    return arr
BUBBLE_SORT = bubble_srot(arr=nums)
print("Bubble Sort    : " , BUBBLE_SORT)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1 , n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return arr
INSERTION_SORT = insertion_sort(arr=nums)
print("Insertion Sort : " , INSERTION_SORT)