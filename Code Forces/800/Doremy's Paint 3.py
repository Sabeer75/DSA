t = int(input())

for _ in range(t): 
    n = int(input())
    a = list(map(int,input().split()))

    mapl = {}
    for i in a:
        if i in mapl:
            mapl[i] += 1 
        else:
            mapl[i] = 1
    
    if len(mapl) >= 3:
        print("No")
    else:
        lis = sorted(mapl.values())
        if len(lis) == 1 or lis[0] == lis[1] or (n % 2 == 1 and abs(lis[0] - lis[1])) == 1:
            print("Yes")
        else:
            print("No")

