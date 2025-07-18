nums = [1,2,3,4,5,6,7]
n = len(nums)
k = 3



for _ in range(1 , k + 1):
    temp = nums[n - 1]
    for i in range(n - 2 , -1 , -1):
        nums[i + 1] = nums[i]
    nums[0] = temp
    
print(nums)



