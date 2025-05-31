def remove(nums,val):
    values = []
    for i in nums:
        if i != val:
            values.append(i)
    nums.clear()
    k = 0
    for i in values:
        nums.append(i)
        k +=1
    return k,nums
nums = [3,2,2,3,4,5,6,3,7,8]
val = 3
print(remove(nums,val))
