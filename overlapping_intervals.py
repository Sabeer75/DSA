nums = [[1, 3], [2, 4], [9, 10], [6, 8]]
nums.sort()
print(nums)
seq = []
for i in range(len(nums)):
    for j in range(len(nums[i])):
        seq.append(nums[i][j])
seq.sort()
print(seq)
start = 0
end = 0
