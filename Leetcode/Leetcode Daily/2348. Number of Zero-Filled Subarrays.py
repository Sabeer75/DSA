nums = [1, 3, 0, 0, 2, 0, 0]
cnt, streak = 0, 0
for num in nums:
    if num == 0:
        streak += 1
        cnt += streak
    else:
        streak = 0
print(cnt)
