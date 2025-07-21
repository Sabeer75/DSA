nums = [5,4,-1,7,8]

max_sum = 0 
n = len(nums)
for i in range(n):
    curr_sum = 0 
    for j in range(i,n):
        curr_sum += nums[j]
        max_sum = max(max_sum,curr_sum)
print(max_sum)