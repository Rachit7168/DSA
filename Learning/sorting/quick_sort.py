def partition(arr, low, high):
    """
    Partition: Rearrange elements around a pivot so that
    elements <= pivot are to its left, and > pivot are to its right.

    Example Dry Run for input: [5,7,8,4] with pivot=5

    partition([5,7,8,4], low=0, high=3)
        |
        + pivot = 5 (at index 0)
        + i scans right until > pivot
        + j scans left until <= pivot
        + swap elements at i and j if i<j
        |
        + Final swap pivot with arr[j] → pivot placed at its correct position

    Returns: index of pivot in sorted position
    """
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # Move i right while arr[i] <= pivot
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        # Move j left while arr[j] > pivot
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        # Swap out-of-place elements
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    """
    Quick Sort: Recursively partition the array and sort each part.

    Example Dry Run for input: [5,7,8,4]

    quick_sort([5,7,8,4], low=0, high=3)
        |
        + partition([5,7,8,4], 0, 3) → pivot index = 1
        |
        + quick_sort(..., 0, 0) → left of pivot
        + quick_sort(..., 2, 3) → right of pivot
        |
        (Continue recursively)

    Result: array sorted in-place
    """
    if low < high:
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index - 1)     # Left partition
        quick_sort(arr, p_index + 1, high)   # Right partition


# Input array
nums = [5, 7, 8, 4, 1, 6, 9, 2]

print("Original:", nums)

# Quick Sort (in-place)
quick_sort(nums, 0, len(nums) - 1)
print("Sorted with Quick Sort:", nums)

# Merge Sort (returns new array)
