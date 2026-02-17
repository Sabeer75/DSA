class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        res = []
        # create a empty row*col array with False filled in it
        visited = [[False] * n for i in range(n)]

        # first bloack 0 then return null
        if maze[0][0] == 0:
            return []

        def backtrack(r, c, path):
            if r == n - 1 and c == n - 1:
                res.append(path)
                return

            visited[r][c] = True

            # lexicographical order + check if the  l R U D blocks are valid to move
            if r + 1 < n and maze[r + 1][c] == 1 and not visited[r + 1][c]:
                backtrack(r + 1, c, path + "D")

            if c - 1 >= 0 and maze[r][c - 1] == 1 and not visited[r][c - 1]:
                backtrack(r, c - 1, path + "L")

            if c + 1 < n and maze[r][c + 1] == 1 and not visited[r][c + 1]:
                backtrack(r, c + 1, path + "R")

            if r - 1 >= 0 and maze[r - 1][c] == 1 and not visited[r - 1][c]:
                backtrack(r - 1, c, path + "U")
            # backtrack update array
            visited[r][c] = False

        backtrack(0, 0, "")
        return res
