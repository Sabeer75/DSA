people = [2, 1, 2, 3]
limit = 3
people.sort()

i = 0
j = len(people) - 1
count = 0

while i <= j:
    if people[i] + people[j] <= limit:
        i += 1
    j -= 1
    count += 1
print(count)
