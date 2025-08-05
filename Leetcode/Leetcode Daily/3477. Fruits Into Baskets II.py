fruits = [4, 2, 5]
baskets = [3, 5, 4]

count = 0
n = len(fruits)

for i in fruits:
    unset = 1
    for j in range(n):
        if i <= baskets[j]:
            baskets[j] = 0
            unset = 0
            break
    count += unset
print(count)
