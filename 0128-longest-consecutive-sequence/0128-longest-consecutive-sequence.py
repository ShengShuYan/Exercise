import heapq
class Solution:
    def longestConsecutive(self, num: List[int]) -> int:
        if not num:
            return 0
        nums = set(num)
        L = 1
        for i in nums:
            if i - 1 not in nums:
                l = 1
                while l + i in nums:
                    l += 1
                L = max(L, l)
        return L
