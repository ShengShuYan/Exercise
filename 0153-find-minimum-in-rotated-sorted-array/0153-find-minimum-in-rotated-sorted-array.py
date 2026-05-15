class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        ans = nums[0]
        while start < end:
            mid = (start+end)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return nums[start]
