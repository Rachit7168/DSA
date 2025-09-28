nums = [3,3,4]

fre_map = {}

for i in range(0 , len(nums)):
    fre_map[nums[i]] = fre_map.get(nums[i] , 0) + 1
    

print(max(fre_map , key=fre_map.get))
print(fre_map)


