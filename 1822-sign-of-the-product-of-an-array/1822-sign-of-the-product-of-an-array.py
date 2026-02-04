class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for c in nums:
            if c == 0:
                return 0
            elif c < 0:
                ans *= -1
        return ans

        