nums1 = [1,2,3]
m = 3 
nums2 = [2,5,6]
n = 3

# Extend nums1 to length m+n
while len(nums1) < m + n:
    nums1.append(0)

# Copy both arrays' relevant parts into one list, sort it
merged = sorted(nums1[:m] + nums2)

# Update nums1 in place
for i in range(m + n):
    nums1[i] = merged[i]

print(nums1)
