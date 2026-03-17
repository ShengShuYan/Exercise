class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        now = [0] * n
        result = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    now[j] = 0
                else:
                    now[j] += 1
            sort = sorted(now, reverse = True)
            for _ in range(n):
                result = max(result, sort[_]*(_+1))

        return result



        