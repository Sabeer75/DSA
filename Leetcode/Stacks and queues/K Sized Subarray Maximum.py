from collections import deque


def maxOfSubarrays(arr, k):
    dq = deque()
    res = []

    for i in range(len(arr)):

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            res.append(arr[dq[0]])

    return res


arr_1 = [1, 2, 3, 4, 6, 8, 5]
print(maxOfSubarrays(arr_1, 3))
