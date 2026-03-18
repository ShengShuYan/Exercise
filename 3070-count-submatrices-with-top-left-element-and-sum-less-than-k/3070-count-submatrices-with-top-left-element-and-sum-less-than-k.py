class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0
        col_max = len(grid[0])
        row_max = len(grid)
        col = col_max
        row = row_max

        for i in range(1, col_max):
            grid[0][i] += grid[0][i-1]
            if grid[0][i] > k:
                col = i
                break

        count = col
        colsum = grid[0][0]

        for j in range(1, row_max):
            colsum += grid[j][0]
            if colsum > k:
                break
            
            i = 1
            while i < col:
                if j > 1:
                    grid[j-1][i] += grid[j-2][i]
                grid[j][i] += grid[j][i-1]
                if grid[j][i] + grid[j-1][i] > k:
                    col = i
                    break
                i += 1
            count = count + col

        return count
     