class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row_S = set()
        col_S = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_S.add(i)
                    col_S.add(j)

        for m in row_S:
            for n in range(col):
                matrix[m][n] = 0

        for a in col_S:
            for b in range(row):
                matrix[b][a] = 0
            