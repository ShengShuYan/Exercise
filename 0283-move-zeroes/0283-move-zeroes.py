class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        l = 0
        for i in range(L):
            if nums[i] != 0:
                nums[l] = nums[i]
                l += 1
        for i in range(l, L):
            nums[i] = 0
        
        
        
        
        