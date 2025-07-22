nums = [4,2,4,5,6]
l = 0 
sett = set()
curr_sum = 0
max_sum = 0 

for r in range(len(nums)):
    while nums[r] in sett:
        sett.remove(nums[l])
        curr_sum -= nums[l]
        l += 1
    sett.add(nums[r])
    curr_sum += nums[r]

    max_sum = max(curr_sum,max_sum)
print(max_sum)