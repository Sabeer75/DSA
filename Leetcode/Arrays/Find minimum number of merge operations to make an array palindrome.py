nums = [11, 14, 15, 99]
l = 0
r = len(nums) - 1
count = 0
while l <= r:
    if nums[l] == nums[r]:
        l += 1
        r -= 1
    elif nums[l] < nums[r]:
        l += 1
        nums[l] += nums[l - 1]
        count += 1
    else:
        r -= 1
        nums[r] += nums[r + 1]
        count += 1
print(count)
