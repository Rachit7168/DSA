nums = [9,2,6,5,0,1,9,6,1,9]


#method 1 :
freq_map = {}

for i in range(0 , len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)

#methods 2 

n = len(nums)

hash_map = {}
for i in range(0 , n):
    hash_map[nums[i]] = hash_map.get(nums[i] , 0) + 1
    
print(hash_map)