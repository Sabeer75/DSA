arr = [1, 2, 3, 4, 5, 6]


def f(l, r):
    if l >= r:
        print(arr)
        return
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp

    f(l + 1, r - 1)


f(0, len(arr) - 1)
