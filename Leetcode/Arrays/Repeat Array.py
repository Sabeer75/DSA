from collections import defaultdict

li = [3, 1, 2, 5, 3]
dict = defaultdict(int)

for i in range(len(li)):
    dict[li[i]] += 1
print(dict)
for k, v in dict.items():
    if v > 1:
        print(k)
