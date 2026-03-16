import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        m = len(grid)
        n = len(grid[0])
        l = m + n - 1

        vals = [[0]*l for _ in range(l)]
        for i in range(m):
            for j in range(n):
                u = i + j
                v = i - j + n - 1
                vals[u][v] = grid[i][j]

        prefix = [[0]*(l+1) for _ in range(l+1)]

        for i in range(l):
            row = vals[i]
            pref_row = prefix[i + 1]
            prev_row = prefix[i]
            for j in range(l):
                pref_row[j + 1] = pref_row[j] + prev_row[j + 1] - prev_row[j] + row[j]

        heap = []
        seen = set()
        for i in range(m):
            for j in range(n):
                u0 = i + j
                v0 = i - j + n - 1
                max_r = min(i, m - 1 - i, j, n - 1 - j)
                for r in range(max_r + 1):
                    x1, x2 = u0 - r, u0 + r
                    y1, y2 = v0 - r, v0 + r
                    outer = (prefix[x2 + 1][y2 + 1] - prefix[x1][y2 + 1] -
                             prefix[x2 + 1][y1] + prefix[x1][y1])
                    if r == 0:
                        rhombus = outer
                    else:
                        x1_in, x2_in = u0 - (r - 1), u0 + (r - 1)
                        y1_in, y2_in = v0 - (r - 1), v0 + (r - 1)
                        inner = (prefix[x2_in + 1][y2_in + 1] - prefix[x1_in][y2_in + 1] -
                                 prefix[x2_in + 1][y1_in] + prefix[x1_in][y1_in])
                        rhombus = outer - inner
                    if len(heap) == 3 and rhombus < heap[0]:
                        continue
                    if rhombus not in seen:
                        seen.add(rhombus)
                        heapq.heappush(heap, rhombus)
                        if len(heap) > 3:
                            heapq.heappop(heap)

        return sorted(heap, reverse=True)