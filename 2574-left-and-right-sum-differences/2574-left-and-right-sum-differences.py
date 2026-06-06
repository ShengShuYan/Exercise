class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [0] * n
        r = [0] * n
        ans = [0] * n
        for i in range(1, n):
            l[i] = l[i-1] + nums[i-1]

        for j in range(n-2, -1, -1):
            r[j] = r[j+1] + nums[j+1]

        for z in range(n):
            ans[z] = abs(l[z] - r[z])

        return ans
