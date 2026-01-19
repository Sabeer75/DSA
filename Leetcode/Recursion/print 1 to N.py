name = "sabeer"
n = 10
i = 0


def f(i, n):
    if i == n:
        return
    i += 1
    print(i, end=" ")
    f(i, n)


f(i, n)
