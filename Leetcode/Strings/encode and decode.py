strs = ["neet", "code", "love", "you"]
res = ""
for i in strs:
    res += str(len(i)) + "#" + i
print(res)

out = []
i = 0
while i < len(res):
    j = i
    while res[j] != "#":
        j += 1

    length = int(res[i:j])
    word = res[j + 1 : j + 1 + length]
    out.append(word)
    i = j + 1 + length
print(out)
