height = [4,2,0,3,2,5]

prefix = [0] * len(height)

for i in range(len(height)):

    if i == 0:
        prefix[i] = height[i]
    else:
        prefix[i] = max(prefix[i-1], height[i])

print(prefix)

suffix = [0] * len(height)

for i in range(len(height)-1,-1,-1):

    if i == len(height) -1 :
        suffix[i] = height[i]
    else:
        suffix[i] = max(suffix[i+1], height[i])

print(suffix)


max_water = 0 
for i in range(len(height)-1):
    max_water += min(prefix[i],suffix[i]) - height[i] 

print(max_water)

"""
optimised 
nums = [0,1,0,2,1,0,1,3,2,1,2,1]

l_max = float('-inf')
r_max = float('-inf')
total = 0 

l= 0 
r = len(nums) - 1 
while l < r:
    if nums[l] <= nums[r]:
        if l_max > nums[l]: 
            total += l_max - nums[l]
        else:
            l_max = nums[l]
        l += 1 
    else:
        if r_max > nums[r]:
            total += r_max - nums[r]
        else:
            r_max = nums[r]
        r -= 1 
print(total)
"""