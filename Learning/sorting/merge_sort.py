def merge_array(left_arr, right_arr):
    """
    Merge Array: Merge two sorted arrays into one sorted array.

    Example Dry Run for input: [5,7] and [4,8]

    merge_array([5,7], [4,8])
        |
        + Compare 5 and 4 → take 4 → result = [4]
        + Compare 5 and 8 → take 5 → result = [4,5]
        + Left has 7 left → take 7 → result = [4,5,7]
        + Right has 8 left → take 8 → result = [4,5,7,8]

    Final result: [4,5,7,8]
    """
    result = []  # Final merged sorted array
    left_index, right_index = 0, 0
    l, r = len(left_arr), len(right_arr)

    # Compare elements and build sorted result
    while left_index < l and right_index < r:
        if left_arr[left_index] <= right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1

    # Add remaining elements from left_arr if any
    while left_index < l:
        result.append(left_arr[left_index])
        left_index += 1

    # Add remaining elements from right_arr if any
    while right_index < r:
        result.append(right_arr[right_index])
        right_index += 1

    return result


def merge_sort(arr):
    """
    Merge Sort: Recursively split the array, then merge sorted halves.

    Example Dry Run for input: [5,7,8,4]

    merge_sort([5,7,8,4])
        |
        +-- merge_sort([5,7])
        |        |
        |        +-- merge_sort([5]) → [5]
        |        +-- merge_sort([7]) → [7]
        |        +-- merge_array([5], [7]) → [5,7]
        |
        +-- merge_sort([8,4])
                |
                +-- merge_sort([8]) → [8]
                +-- merge_sort([4]) → [4]
                +-- merge_array([8], [4]) → [4,8]

    Finally:
    merge_array([5,7], [4,8]) → [4,5,7,8]
    """
    if len(arr) <= 1:
        # Base case: single element is already sorted
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    # Merge the sorted halves
    return merge_array(left, right)


# Input array
nums = [5, 7, 8, 4, 1, 6, 9, 2]

# Call merge_sort and print result
print(merge_sort(nums))
