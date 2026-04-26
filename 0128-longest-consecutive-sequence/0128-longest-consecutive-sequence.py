import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        cur = heapq.heappop(nums)
        L = 1
        l = 1
        while len(nums) > 0:
            n = heapq.heappop(nums)
            if n - cur == 1:
                l += 1
                L = max(L, l)
            elif n > cur:
                l = 1
            cur = n
        return L
            
            


        