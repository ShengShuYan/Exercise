from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_num = sorted(nums)
        ans = []
        for i in nums:
            ans.append(bisect_left(sort_num, i))

        return ans

        