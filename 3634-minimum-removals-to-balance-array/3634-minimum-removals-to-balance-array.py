class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        res = 0
        j = 0  
        
        for i in range(n):
            while j < n and nums[j] <= k * nums[i]:
                j += 1
            
            res = max(res, j - i)
        
        return n - res