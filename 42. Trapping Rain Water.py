height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
count = 0
nums = height
l = r = 0
for r in range(len(nums) - 1):
    if nums[r] > nums[l]:
        l = r
    if max(nums[r + 1 :]) > nums[l]:
        count += nums[l] - nums[r]
    else:
        l = nums.index(max(nums[r + 1 :]))
        if nums[l] - nums[r] >= 0:
            count += nums[l] - nums[r]
print(count)
