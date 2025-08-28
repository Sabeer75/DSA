intervals = [[1, 3], [2, 4], [9, 10], [6, 8]]
intervals.sort(key=lambda x: x[0])
output = [intervals[0]]

for s, e in intervals[1:]:
    last = output[-1][1]
    if s <= last:
        output[-1][1] = max(e, last)
    else:
        output.append([s, e])
print(output)
