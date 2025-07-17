nums = [-4,-1,0,15,34]
res = []
l = 0 
r = len(nums) - 1 

while l <= r:
    if abs(nums[l]) > abs(nums[r]):
        res.append(nums[l]**2)
        l += 1 
    else:
        res.append(nums[r]**2)
        r -= 1 
print(res[::-1]) #timecomplexity = O(n)

'''
squared = []
for i in nums:
    squared.append(i*i)

print(sorted(squared))
# time complexity is O(n log n)
'''