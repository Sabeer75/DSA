matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

t, b = 0, len(matrix)
l, r = 0, len(matrix[0])
res = []

"""
Right: (0, 1) - row stays same, column increases
Down: (1, 0) - row increases, column stays same
Left: (0, -1) - row stays same, column decreases
Up: (-1, 0) - row decreases, column stays same
"""
while l < r and t < b:
    for i in range(l, r):
        res.append(matrix[l][i])
    t += 1

    for i in range(t, b):
        res.append(matrix[i][r - 1])
    r -= 1

    if not (l < r and t < b):
        break

    for i in range(r - 1, l - 1, -1):
        res.append(matrix[b - 1][i])
    b -= 1

    for i in range(b - 1, t - 1, -1):
        res.append(matrix[i][l])
    l += 1
print(res)
