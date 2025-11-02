class Solution:
    def countUnguarded(self, m: int, n: int, g: list[list[int]], w: list[list[int]]) -> int:
        vis = [[0] * n for _ in range(m)]
        
        for val in w:
            vis[val[0]][val[1]] = 2

        for val in g:
            vis[val[0]][val[1]] = 3

        for val in g:
            row, col = val[0], val[1]

            for i in range(row + 1, m):
                if vis[i][col] in (2, 3):  
                    break
                vis[i][col] = 1 

            for i in range(row - 1, -1, -1):
                if vis[i][col] in (2, 3):
                    break
                vis[i][col] = 1

            for i in range(col + 1, n):
                if vis[row][i] in (2, 3):
                    break
                vis[row][i] = 1

            for i in range(col - 1, -1, -1):
                if vis[row][i] in (2, 3):
                    break
                vis[row][i] = 1

        unguarded = 0
        for i in range(m):
            for j in range(n):
                if vis[i][j] == 0:
                    unguarded += 1

        return unguarded
