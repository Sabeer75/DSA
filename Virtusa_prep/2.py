list_1 = [21, 2, 30, 33]
curr_sum = 0
min_sum = float("inf")
for i in range(len(list_1)):
    stri = str(list_1[i])
    for j in stri:
        inte = int(j)
        curr_sum += inte
    min_sum = min(curr_sum, min_sum)
    curr_sum = 0
print(min_sum)
