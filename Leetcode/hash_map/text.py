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

