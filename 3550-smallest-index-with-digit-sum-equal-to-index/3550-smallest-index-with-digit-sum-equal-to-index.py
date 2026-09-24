class Solution:
    def digsum(self, num):
        ans = 0
        while num > 0:
            ans += num % 10
            num = num // 10
        return ans

    def smallestIndex(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if self.digsum(v) == i:
                return i

        return -1

        