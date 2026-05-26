class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        dp = [0] * n
        dp[0] = 1
        T = 0

        for i in range(1, n):

            if i >= minJump:
                T += dp[i-minJump]
            if i > maxJump:
                T -= dp[i-maxJump-1]

            if s[i] == '0' and T > 0:
                dp[i] = 1

        return bool(dp[n-1])