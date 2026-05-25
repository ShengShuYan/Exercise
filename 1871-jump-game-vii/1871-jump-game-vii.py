class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        ini = 0
        T = 0

        for i in range(minJump, n):
            if s[i] == '0':
                if not ini:
                    if i <= maxJump:
                        T = 1
                    else:
                        return False
                    ini = 1
                if T > 0:
                    dp[i] = 1
            if ini and i-maxJump >= 0:
                T = T - dp[i-maxJump]
            if ini and i-minJump+1 < n:
                T += dp[i-minJump+1]
                
        return bool(dp[n-1])
        