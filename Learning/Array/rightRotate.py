nums = [1 , 2 , 3 , 4 , 5]
n = len(nums)

nums[:] = [nums[-1]] + nums[0:n-1]
print(nums)
