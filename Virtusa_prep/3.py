no_of_elements = int(input())
elements = [int(input()) for _ in range(no_of_elements)]
elements.sort()
print(elements)

current_sum = 1
max_sum = float("-inf")
for i in range(1, len(elements)):
    if elements[i] - elements[i - 1] == 1:
        current_sum += 1
        max_sum = max(max_sum, current_sum)
    else:
        current_sum = 1
print(max_sum)
