arr = [1, 2, 3, 4, 5, 6, 7, 8]
M = 3
if M == 0 or len(arr) < M:
    print(0)

arr.sort()
min_diff = float("inf")
for i in range(len(arr) - M + 1):
    curr_diff = arr[i + M - 1] - arr[i]
    min_diff = min(curr_diff, min_diff)
print(min_diff)
