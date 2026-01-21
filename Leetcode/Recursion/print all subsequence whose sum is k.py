# print all subsequence whose sum is k

k = 2
arr = [1, 2, 1]
n = []
summ = 0


def f(i, n, summ):
    if i == len(arr):
        if summ == k:
            print(n)
        return

    n.append(arr[i])
    summ += arr[i]
    f(i + 1, n, summ)

    summ -= arr[i]
    n.pop()
    f(i + 1, n, summ)


f(0, n, summ)
