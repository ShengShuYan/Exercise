class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = 0
        mis = 0
        cur = 1

        for i in range(len(nums)):
            if nums[i] != cur:
                if nums[i] == cur - 1:
                    dup = nums[i]
                elif nums[i] == cur + 1:                   
                    mis = cur
                    cur = cur + 2
            else:
                cur = cur + 1
        
        if mis == 0:
            mis = cur
        return [dup, mis]


        