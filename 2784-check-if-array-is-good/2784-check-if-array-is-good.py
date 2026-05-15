class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        ans = [0] * n
        for i in nums:
            if i > n or (i < n and ans[i-1] > 0) or (i == n and ans[i-1]>1):
                return False
            else:
                ans[i-1] += 1

        return True

        
        