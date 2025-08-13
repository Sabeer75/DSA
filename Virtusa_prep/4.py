S1 = "abcoaching"
S2 = "coding"

n = len(S2)
similar = 0
j = 0
for i in range(len(S2)):
    if S1[i] == S2[j]:
        if S1[i] == S2[j]:
            similar += 1
            j += 1
print(n - similar)
