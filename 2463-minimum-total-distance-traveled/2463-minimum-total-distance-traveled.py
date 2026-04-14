class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)

        dp = [[float('inf')] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            pos, lim = factory[i-1]
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                dsum = 0
                for k in range(1, min(j,lim)+1):
                    dsum += abs(robot[j-k]-pos)
                    if dp[i-1][j-k]!=float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i-1][j-k]+dsum)

        return dp[n][m]
