from collections import defaultdict

fruits = [1, 2, 1]
two = defaultdict(int)
counter = float("-inf")
# l = 0 and r= 0
l = 0
for r in range(len(fruits)):
    two[fruits[r]] += 1
    while len(two) > 2:
        two[fruits[l]] -= 1
        if two[fruits[l]] == 0:
            del two[fruits[l]]
        l += 1
    size = r - l + 1
    counter = max(counter, size)
print(counter)
# r += 1 and add to dict until u get more than 2 len in dict
# if so get the len of sliding window set to max
# then move r pointer
# return max
