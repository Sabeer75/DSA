num = 9669
list_1 = []
for i in str(num):
    list_1.append(int(i))
for i in range(len(list_1)):
    if list_1[i] == 6:
        list_1[i] = 9
        break
print(int("".join(map(str, list_1))))
