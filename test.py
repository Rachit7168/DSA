nums = [9,2,6,5,0,1,9,6,1,9]


freq_map = {}

for i in range(0 , len(nums)):
    freq_map[nums[i]] = freq_map.get(nums[i] , 0) + 1
    print(freq_map)

