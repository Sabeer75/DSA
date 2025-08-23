height = [0,1,0,2,1,0,1,3,2,1,2,1]
f= 0 
rcount=0
for i in range(len(height[f+1:])):
    if height[f]<=height[i]:
        rcount+=height[f]*(i-f+1)-sum(height[f:i])+f
        f = i 
    else:
        i = max(height[f:])
        rcount += height[i]*(i-f+1) - sum(height[f+1:i+1])+i
        f = i 
print(rcount)