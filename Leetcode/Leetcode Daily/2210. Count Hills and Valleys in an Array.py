nums = [2, 4, 1, 1, 6, 5]
final = [nums[0]]
for i in range(1, len(nums)):
    if nums[i] != final[-1]:
        final.append(nums[i])

count = 0
for i in range(1, len(final) - 1):
    if final[i - 1] < final[i] > final[i + 1]:
        count += 1
    elif final[i - 1] > final[i] < final[i + 1]:
        count += 1
print(count)
