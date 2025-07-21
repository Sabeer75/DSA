nums = [1,2,3,4]
ans = []
for i in range(len(nums)+1):
    l = i 
    r = i 
    while l >= 0 and r <= len(nums):
        l -= 1
        r += 1 
        print(i)