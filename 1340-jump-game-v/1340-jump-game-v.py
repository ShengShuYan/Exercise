class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n

        def dfs(i):
            if dp[i] != 0:
                return dp[i]

            max_j = 1
            
            for j in range(i+1, min(i+d+1,n)):
                if arr[j] >= arr[i]:
                    break
                max_j = max(max_j, 1+dfs(j))
                

            for j in range(i-1, max(i-d-1,-1), -1):
                if arr[j] >= arr[i]:
                    break
                max_j = max(max_j, 1+dfs(j))

            dp[i] = max_j

            return max_j

        return max(dfs(i) for i in range(n))

        