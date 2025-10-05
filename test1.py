"""
#fibonacci

a = 0
b = 1

for _ in range(5):
    print(a)
    a, b = b, a + b
"""

"""
# armstrong s number

n = 153
length = len(str(n))
sum = 0
for i in str(n):
    sum += int(i) ** length
if sum == n:
    print("It is an armstrong number")
else:
    print("it is not an armstrong s number")
"""


"""
# palindrome number/string

s = "12321"
l, r = 0, len(s) - 1
is_palindrome = True
while l <= r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        is_palindrome = False
        break

if is_palindrome:
    print("yes it is palindrome")
else:
    print("it is not palindrome")
"""


"""
# factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))
"""

"""
# prime number
n = 2
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("prime")
else:
    print("it is not prime")
"""

"""
# Reverse an Array
arr = [1, 2, 3, 4, 5]
l = 0
r = len(arr) - 1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
print(arr)
"""

"""
# right and left shift 
def left(k):
    left_shift = arr[k:] + arr[:k]
    return left_shift


def right(k):
    right_shift = arr[-k:] + arr[:-k]
    return right_shift


arr = [1, 2, 3, 4, 5]
print(left(2))
print(right(1))
"""

for i in range(1, 6):
    print("*" * i)
