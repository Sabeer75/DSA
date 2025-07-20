t = int(input ())

for _ in range(t): 
    n = int(input())
    a = list(map(int,input().split()))

    if n == 2:
        print("Yes")
    elif n == 3:
        if a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
            print("Yes")
        else:
            print("No")
    elif len(set(a)) == 1:
        print("Yes")
    else:
        print("No")