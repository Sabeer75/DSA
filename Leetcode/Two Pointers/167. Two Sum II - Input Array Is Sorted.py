nums = [3,24,50,79,88,150,345]
target = 200

l = 0 
r = len(nums) -1

while l < r and r < len(nums)-1:
    if nums[l] + nums[r] == target:
                print([l+1,r+1])
                break

    if nums[l] + nums[r] > target:
        r -= 1 
    else:
        l += 1 