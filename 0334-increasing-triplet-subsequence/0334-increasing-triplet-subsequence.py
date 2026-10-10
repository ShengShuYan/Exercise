class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)
        pre = [False] * n
        vmin = nums[0]
        for i in range(n):
            pre[i] = nums[i] > vmin
            vmin = min(vmin, nums[i])
        vmax = nums[-1]
        for j in range(n-1, -1, -1):
            if nums[j] < vmax and pre[j]:
                return True
            vmax = max(vmax, nums[j])
        return False
        
