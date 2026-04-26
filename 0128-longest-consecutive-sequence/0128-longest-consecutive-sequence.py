import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        L = 1
        for i in nums:
            if i - 1 not in nums:
                l = 1
                while l + i in nums:
                    l += 1
                L = max(L, l)
        return L
