A = [0]
ans = set()
cur = {0}
for x in A:
    cur = {x | y for y in cur} | {x}
    ans |= cur
print(len(ans))
