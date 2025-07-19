nums = [-1,5,7,0]
A = []
B = []
for i in range(nums):
    is_prime = True 
    for j in range(2,int(nums[i]**0.5)+1):
        if nums[i] % j == 0:
            B.append(nums[i])
        else:
            A.append(nums[i])
A_t = sum(A)
B_t = sum(B)
print(A_t - B_t)