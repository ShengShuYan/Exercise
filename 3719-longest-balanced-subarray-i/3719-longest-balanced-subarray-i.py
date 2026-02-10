class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for left in range(n):
            even_set = set()
            odd_set = set()
            for right in range(left, n):
                x = nums[right]
                if x % 2 == 0:
                    even_set.add(x)
                else:
                    odd_set.add(x)
                
                if len(even_set) == len(odd_set):
                    res = max(res, right - left + 1)
        
        return res
        

        