nums = [5, 7, 8, 4, 1, 6, 9, 2]
# 5 7 8 8 1 
# 5 7 7 8
# 5 5 7 8
# 4 5 7 8
n = len(nums)
for i in range(1, n):  # i = index of the "key" to insert
    key = nums[i]      # current element to insert
    j = i - 1
    # Shift all elements > key one position to the right
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key  # insert key in correct position

    # Dry run output after each outer loop (i-th pass):
    # i=1: key=7 → already in place → [5,7,8,4,1,6,9,2]
    # i=2: key=8 → already in place → [5,7,8,4,1,6,9,2]
    # i=3: key=4 → insert before 5 → [4,5,7,8,1,6,9,2]
    # i=4: key=1 → insert at start → [1,4,5,7,8,6,9,2]
    # i=5: key=6 → insert before 7 → [1,4,5,6,7,8,9,2]
    # i=6: key=9 → already in place → [1,4,5,6,7,8,9,2]
    # i=7: key=2 → insert after 1 → [1,2,4,5,6,7,8,9]

print(nums)
