class Solution:
    def canJump(self, nums: list[int]) -> bool:
        tar = len(nums) - 1
        i = tar-1
        while i>=0 and i!= tar:
            step = nums[i]
            if i+step >= tar:
                tar = i
                i = tar-1
            else:
                i -= 1
        return tar == 0
