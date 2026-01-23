arr = [10, 20, 30]
n = len(arr)
prev_smaller = [-1] * n

stack = [0]
for i in range(1, n):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()

    if stack:
        prev_smaller[i] = stack[-1]
    stack.append(i)

print(prev_smaller)

next_smaller = [n] * n
stack = [n - 1]
for i in range(n - 2, -1, -1):
    while stack and arr[i] <= arr[stack[-1]]:
        stack.pop()
    if stack:
        next_smaller[i] = stack[-1]
    stack.append(i)
print(next_smaller)

res = [-1] * n
for i in range(n):
    window = next_smaller[i] - (prev_smaller[i] + 1)
    res[window - 1] = max(res[window - 1], arr[i])

print(res)

for i in range(n - 2, -1, -1):
    res[i] = max(res[i], res[i + 1])

print(res)
