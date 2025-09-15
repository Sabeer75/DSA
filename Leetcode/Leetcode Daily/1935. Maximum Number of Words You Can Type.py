from collections import defaultdict

text = "leet code"
brokenLetters = "e"
broken = defaultdict(int)

for i in brokenLetters:
    broken[i] = 1

splitted = text.split()
count = 0
for i in splitted:
    for j in i:
        if broken[j] == 1:
            valid = False
            break
    if valid:
        count += 1
print(count)
