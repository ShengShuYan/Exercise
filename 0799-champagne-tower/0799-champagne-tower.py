class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current = [poured]
        for row in range(1, query_row + 1):
            next_row = [0.0] * (row + 1)
            for j in range(row):
                overflow = max(0.0, current[j] - 1.0)
                if overflow > 0:
                    next_row[j] += overflow / 2.0
                    next_row[j + 1] += overflow / 2.0
            current = next_row

        return min(1.0, current[query_glass])
        