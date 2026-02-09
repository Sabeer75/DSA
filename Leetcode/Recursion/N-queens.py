class Solution:
    def solveNQueens(self, n):
        col = set()  # q placed in columns
        posdia = set()  # q placed in positive diagnols(r+c)
        negdia = set()  # q placed in negative diagnols(r-c)
        res = []
        board = [["."] * n for i in range(n)]  # empty board

        def backtrack(c):
            if c == n:
                copy = [
                    "".join(row) for row in board
                ]  # copy is appended in res because board empty array should be used again
                res.append(copy)
                return

            for r in range(n):
                if (
                    r in col or (r + c) in posdia or (r - c) in negdia
                ):  # checks if the current queen can be attacked by other placed queens
                    continue

                # place the queen updates set
                col.add(r)
                posdia.add(r + c)
                negdia.add(r - c)
                board[r][c] = "Q"

                # go deeper into other columns
                backtrack(c + 1)

                # while backtracking remove the queens trace and update the board
                col.remove(r)
                posdia.remove(r + c)
                negdia.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
