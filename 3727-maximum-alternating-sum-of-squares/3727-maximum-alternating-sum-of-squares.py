class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [x**2 for x in nums]
        nums.sort()
        ans = 0
        for i in range(len(nums)//2):
            ans -= nums[i]
        for j in range(len(nums)//2, len(nums)):
            ans += nums[j]
        return ans