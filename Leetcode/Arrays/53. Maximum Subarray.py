#kadanes algorithm 
nums = [5,4,-1,7,8]
max_sum = float('-inf')
curr_sum = 0 
for i in range(len(nums)):
    curr_sum += nums[i]
    max_sum = max (curr_sum , max_sum )
    if curr_sum < 0:
        curr_sum = 0 
print(max_sum)

''' 
#bruteforce 
nums = [5,4,-1,7,8,9]

max_sum = 0 
n = len(nums)
for i in range(n):
    curr_sum = 0 
    for j in range(i,n):
        curr_sum += nums[j]
        max_sum = max(max_sum,curr_sum)
print(max_sum)
'''   
