nums = [5, 7, 8, 4, 1, 6, 9, 2]

def selection_sort(array):  # --> ascending
    n = len(array)
    for i in range(0, n):
        minimun = i
        # Find the smallest element in the unsorted part
        for j in range(i + 1, n):
            if array[j] < array[minimun]:
                minimun = j
        # Swap the found minimum element with the first unsorted element
        nums[i], nums[minimun] = nums[minimun], nums[i]
        # Dry run output after each pass:
        # Pass 1 (i=0): swap 5 and 1 → [1, 7, 8, 4, 5, 6, 9, 2]
        # Pass 2 (i=1): swap 7 and 2 → [1, 2, 8, 4, 5, 6, 9, 7]
        # Pass 3 (i=2): swap 8 and 4 → [1, 2, 4, 8, 5, 6, 9, 7]
        # Pass 4 (i=3): swap 8 and 5 → [1, 2, 4, 5, 8, 6, 9, 7]
        # Pass 5 (i=4): swap 8 and 6 → [1, 2, 4, 5, 6, 8, 9, 7]
        # Pass 6 (i=5): swap 8 and 7 → [1, 2, 4, 5, 6, 7, 9, 8]
        # Pass 7 (i=6): swap 9 and 8 → [1, 2, 4, 5, 6, 7, 8, 9]
        # Pass 8 (i=7): already smallest at last position
    return nums

print(selection_sort(nums))

