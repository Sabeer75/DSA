arr = [7, 9, 1, 3, 5]
target = 6

n = len(arr)
pivot = 0

for i in range(n):
    if arr[i] < arr[i - 1]:
        pivot = i
        break

# 2 pointers to find pair

l = pivot
r = (pivot - 1 + n) % n

found = False
while l != r:
    if arr[l] + arr[r] == target:
        print(True)
        found = True
        break
    elif arr[l] + arr[r] < target:
        l = (l + 1) % n
    else:
        r = (r - 1 + n) % n
if not found:
    print(False)
"""
#my solution with TLE 
l, r = 0, len(arr) - 1

while l <= r:
    m = (l + r) // 2

    if (
        arr[l] + arr[m] == target
        or arr[m] + arr[r] == target
        or arr[r] + arr[l] == target
    ):
        print(True)
        break
    elif arr[l] >= target:
        l = m
    elif arr[r] >= target:
        r = m
    else:
        print(False)
        break
"""
