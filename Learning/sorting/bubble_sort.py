nums = [5, 7, 8, 4, 1, 6, 9, 2]

n = len(nums)
for i in range(n - 2, -1, -1):  # i goes from 6 → 0
    # Each pass bubbles the largest element to position i+1
    is_swaped = False
    for j in range(0, i + 1): # 0 , i+1 = 7 : 6
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            is_swaped = True
    if is_swaped == False:
        break
    # Dry run after each outer loop (i-th pass):
    # i=6 → [5, 7, 4, 1, 6, 8, 2, 9]
    # i=5 → [5, 4, 1, 6, 7, 2, 8, 9]
    # i=4 → [4, 1, 5, 6, 2, 7, 8, 9]
    # i=3 → [1, 4, 5, 2, 6, 7, 8, 9]
    # i=2 → [1, 4, 2, 5, 6, 7, 8, 9]
    # i=1 → [1, 2, 4, 5, 6, 7, 8, 9]
    # i=0 → already sorted

print(nums)