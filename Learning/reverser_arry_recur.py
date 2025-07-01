# ----------------------------------------
# Q6: Reverse Array Using Recursion (Two Pointers)
# ----------------------------------------

# Recursive function to reverse array elements between left and right
def func(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)

# Wrapper function that sets default right index if not provided
def reverse_array(nums, left=0, right=None):
    if right is None:
        right = len(nums) - 1
    func(nums=nums, left=left, right=right)
    return nums

# ----------------------------------------
# Function Calls (Test cases)
# ----------------------------------------

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reverse_array(nums=arr))                   # Full reverse
print(reverse_array(nums=arr, left=2, right=5))  # Partial reverse from index 2 to 5