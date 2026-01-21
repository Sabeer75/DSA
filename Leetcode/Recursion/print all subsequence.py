arr = [3, 1, 2]
n = []


def f(i):
    if i >= len(arr):
        print(n)
        return
    n.append(arr[i])
    f(i + 1)
    n.pop()
    f(i + 1)


f(0)
