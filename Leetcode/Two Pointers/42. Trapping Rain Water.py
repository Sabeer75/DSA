height = [4,2,0,3,2,5]

prefix = [0] * len(height)

for i in range(len(height)):

    if i == 0:
        prefix[i] = height[i]
    else:
        prefix[i] = max(prefix[i-1], height[i])

print(prefix)

suffix = [0] * len(height)

for i in range(len(height)-1,-1,-1):

    if i == len(height) -1 :
        suffix[i] = height[i]
    else:
        suffix[i] = max(suffix[i+1], height[i])

print(suffix)


max_water = 0 
for i in range(len(height)-1):
    max_water += min(prefix[i],suffix[i]) - height[i] 

print(max_water)