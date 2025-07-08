t = int(input())
for _ in range (t):
    n , x = map (int, input().split())
    a = list(map(int, input().split()))
    
    max_gap = a[0]
    for i in range (1,n):
        max_gap = max(max_gap, a[i] - a[i-1])

    max_gap = max (max_gap,2*(x-a[-1]))

    print(max_gap)