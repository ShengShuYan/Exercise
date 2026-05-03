class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for c in nums:
            if c == 0:
                ans = max(ans, cur)
                cur = 0
            else:
                cur += 1

        return max(ans, cur)
            
        