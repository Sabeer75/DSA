height = [1,8,6,2,5,4,8,3,7]
max_Area = float('-inf')

n = len(height)
l = 0 
r = n -1 

while l < r:
    if height[l] < height[r]:
        max_Area = max(max_Area,height[l]*(r-l))
        l += 1
    elif height[l] > height[r]:
        max_Area = max(max_Area,height[r]*(r-l))
        r -= 1
    else:
        max_Area = max(max_Area,height[l]*(r-l))
        if height[l+1] > height[r-1]:
            l+= 1
        else:
            r -= 1 
print(max_Area)