t = int(input ())

for _ in range(t): 
    n = int(input())
    a = list(map(int,input().split()))

    distinct_ele = len(set(a))

    if distinct_ele >= 3:
        print("No") 
    else:
        print(set(a))
            
