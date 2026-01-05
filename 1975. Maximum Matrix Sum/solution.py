class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        nc = 0
        total = 0
        min_abs = 10**5 + 1

        for row in matrix:
            for x in row:
                if x < 0:
                    nc += 1
                ax = abs(x)
                total += ax
                min_abs = min(min_abs, ax)

        if nc % 2 == 0:
            return total
        return total - 2 * min_abs
        
