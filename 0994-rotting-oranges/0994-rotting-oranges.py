from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0: return 0
        t = -1
        while q:
            t += 1
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in [(0,1), (0, -1), (1, 0), (-1,0)]:
                    nr = cr + dr
                    nc = cc + dc
                    if 0<=nr < row and 0<=nc < col and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))

        return t if fresh == 0 else -1
        