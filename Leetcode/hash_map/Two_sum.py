#method - 1

def twoSum(nums , target):
    num_map = {}
    for i , num in enumerate(nums):
        t_num = target - num
        if t_num in num_map:
            return [num_map[t_num] , i]
        num_map[num] = i


nums = [2,7,11,15]
target = 9

print(twoSum(nums=nums , target=target))

#method - 2 

def twoSum1(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return[i ,j]
            
nums = [2,7,11,15]
target = 9

print(twoSum1(nums=nums , target=target))