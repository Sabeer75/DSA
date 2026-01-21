# count all subsequence whose sum is k

k = 2
arr = [1, 2, 1]
summ = 0


def f(i, summ):

    if i == len(arr):
        # condition satisfied
        if summ == k:
            return 1
        # condition not satisfied
        else:
            return 0

    summ += arr[i]
    l = f(i + 1, summ)

    summ -= arr[i]
    r = f(i + 1, summ)

    return l + r


print(f(0, summ))
