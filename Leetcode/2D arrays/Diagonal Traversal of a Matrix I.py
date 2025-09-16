matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
]

rows, cols = len(matrix), len(matrix[0])
# create empty list with the number of diagnol
diagnol = []
for _ in range(rows + cols - 1):
    diagnol.append([])

# append all the values of matrix correspondent to the diagnol
for r in range(rows):
    for c in range(cols):
        diagnol[r + c].append(matrix[r][c])

# reverse only the indes which is present in the odd position
res = []
for i in range(len(diagnol)):
    if i % 2 != 0:
        res.extend(diagnol[i][::-1])
    else:
        res.extend(diagnol[i])
print(res)
