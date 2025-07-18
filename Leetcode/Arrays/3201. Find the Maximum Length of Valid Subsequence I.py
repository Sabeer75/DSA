nums = [1,2,3,4,5,6,7] 
array = [[0,0],[1,1],[0,1],[1,0]] 
res = 0  
for pattern in array: 
    count = 0  
    for num in nums: 
        if num % 2 == pattern[count%2]: 
            count += 1 
    res = max(res,count) 
print(res)
