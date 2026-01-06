from collections import deque


class Solution:
    def orangesRot(self, mat):
        n = len(mat)
        m = len(mat[0])
        fresh = 0

        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = -1
        while q:
            minutes += 1

            for _ in range(len(q)):

                x, y = q.popleft()

                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

                for dx, dy in directions:
                    if 0 <= x + dx < n and 0 <= y + dy < m and mat[x + dx][y + dy] == 1:
                        mat[x + dx][y + dy] = 2
                        fresh -= 1
                        q.append((x + dx, y + dy))

        return minutes if fresh == 0 else -1
