class Solution:
    def canJump(self, nums: list[int]) -> bool:
        l = len(nums)
        if l == 1: return True
        dp = [False] * l
        dp[l-1] = True
        for i in range(l-2, -1, -1):
            step = nums[i]
            if step >= l-1-i:
                dp[i] = True
                continue
            else:
                dp[i] = any(x for x in dp[i+1:i+step+1])
        return dp[0]
