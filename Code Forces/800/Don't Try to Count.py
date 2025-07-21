def check(s, x):
    if len(x) < len(s):
        return False
    for i in range(len(x) - len(s) + 1):
        if x[i:i+len(s)] == s:
            return True
    return False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()

    x0 = x             
    x1 = x0 + x0      
    x2 = x1 + x1      
    x3 = x2 + x2        
    x4 = x3 + x3        
    x5 = x4 + x4         

    ans = -1
    if check(s, x0):
        ans = 0
    elif check(s, x1):
        ans = 1
    elif check(s, x2):
        ans = 2
    elif check(s, x3):
        ans = 3
    elif check(s, x4):
        ans = 4
    elif check(s, x5):
        ans = 5

    print(ans)
