#method - 1

def containsDuplicate(nums):
    num_hash ={}
    for i in range(0 , len(nums)):
        if nums[i] in num_hash:
            return True
        num_hash[nums[i]] = i
    return False

#method - 2

def containsDuplicate(nums):
    return True if len(set(nums)) < len(nums) else False