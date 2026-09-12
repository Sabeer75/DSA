import sys

input = sys.stdin.read

score = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

data = input().split()

t = int(data[0])
index = 1

for _ in range(t):

    grid = []

    for i in range(10):
        grid.append(data[index])
        index += 1

    total_score = 0

    for i in range(10):
        for j in range(10):

            if grid[i][j] == 'X':
                total_score += score[i][j]

    print(total_score)