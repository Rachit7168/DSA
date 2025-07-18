nums = [6, 6, 7, 9, 9, 2, 1, 6]

seen = set()
i = 0

for j in range(len(nums)):
    if nums[j] not in seen:
        seen.add(nums[j])
        nums[i] = nums[j]
        i += 1

print(nums[:i])   # unique elements
