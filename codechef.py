T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    A = list(map(int, input().split()))

    max_a = max(A)
    min_a = min(A)

    has_less = False
    for f in A:
        if f < C:
            has_less = True
            break

    has_equal = False
    for f in A:
        if f == C:
            has_equal = True
            break

    if has_less and not has_equal:
        print(0)
    else:
        extra = 1
        while True:
            alice_cookies = C + extra
            equal_found = False
            for f in A:
                if f == alice_cookies:
                    equal_found = True
                    break
            if not equal_found:
                less_found = False
                for f in A:
                    if f < alice_cookies:
                        less_found = True
                        break
                if less_found:
                    print(extra)
                    break
            extra += 1
