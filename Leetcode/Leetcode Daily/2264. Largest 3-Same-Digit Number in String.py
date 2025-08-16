num = "324927583"
list_1 = []

for i in range(1, len(num) - 1):
    if num[i] == num[i - 1] and num[i] == num[i + 1]:
        list_1.append(num[i])

if len(list_1) >= 1:
    maxi = max(list_1)
    s = str(maxi)
    print(s + s + s)
else:
    print("")
