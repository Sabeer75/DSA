n = int(input())
s = [input() for _ in range(n)]
combined = "".join(s).lower()
print(combined)
seen = set()
for i in range(len(combined)):
    seen.add(combined[i])

if len(seen) == 26:
    print(True)
else:
    print(False)
