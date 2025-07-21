s = "aaabaaaa"
s1 = list(s)

res = []

for i in range(len(s1)):
    if i == 0 or i == len(s1)-1:
        res.append(s1[i])
    elif not(s1[i-1] == s1[i] and s1[i+1] == s1[i]):
        res.append(s1[i])

print("".join(res))



