nums = [-20,20]
seen = set()
max_neg = float('-inf')
for i in range(len(nums)):
    if nums[i] < 0:
        #inside are all -ve
        max_neg = max(max_neg,nums[i])
        continue
    seen.add(nums[i])
        
    if seen:
        print(sum(seen))
    else:
        print(max_neg)