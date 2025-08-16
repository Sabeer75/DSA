def isPowerOfFour(n):
    if n <= 0:
        print(False)
    else:
        while n % 4 == 0:
            n //= 4
    return n == 1


n = 24
print(isPowerOfFour(n))
