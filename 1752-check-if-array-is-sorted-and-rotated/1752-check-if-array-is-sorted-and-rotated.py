class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n == 0: return True
        count = 0
        if nums[0] < nums[n]:
            count += 1        
        for i in range(n):
            if nums[i+1] < nums[i]:
                count += 1
            if count > 1:
                return False

        return True




        