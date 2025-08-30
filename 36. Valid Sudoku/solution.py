class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue

                boxIdx = (i // 3) * 3 + (j // 3)

                if c in rows[i] or c in cols[j] or c in blocks[boxIdx]:
                    return False

                rows[i].add(c)
                cols[j].add(c)
                blocks[boxIdx].add(c)

        return True
