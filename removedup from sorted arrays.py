def rd(nums):
    k = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k
nums = [0,1,2,3,3,4,4,5,6,7,7,8,8,9]
print(rd(nums))

