class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        diagonals = [[] for _ in range(rows + cols - 1)]
        for r in range(rows):
            for c in range(cols):
                diagonals[r + c].append(mat[r][c])
        ans = []
        need_reversed = 1
        for diagonal in diagonals:
            if need_reversed:
                ans.extend(diagonal[::-1])
            else:
                ans.extend(diagonal[:])
            need_reversed = 1 - need_reversed
        return ans
