import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = [x for x in nums if x < k]
        heapq.heapify(nums)
        count = 0
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            n = min(x, y) * 2 +max(x,y)
            if n < k:
                heapq.heappush(nums, n)
            count += 1
        if len(nums) == 1 and nums[0] < k:
            return count + 1
        return count
            
        

        