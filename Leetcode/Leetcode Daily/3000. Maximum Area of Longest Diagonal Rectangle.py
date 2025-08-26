dimensions = [[9, 3], [8, 6]]
max_dia_sq = 0
max_area = 0
for l, w in dimensions:
    dia_sq = l * l + w * w
    area = l * w
    if dia_sq > max_dia_sq:
        max_dia_sq = dia_sq
        max_area = area
    elif dia_sq == max_dia_sq:
        max_area = max(max_area, area)
print(max_area)
