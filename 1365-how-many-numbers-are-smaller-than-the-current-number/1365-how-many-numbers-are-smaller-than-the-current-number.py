from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_num = sorted(nums)
        ans = [0]*len(nums)
        dic = {}
        for i in range(len(sort_num)):
            if sort_num[i] not in dic:
                dic[sort_num[i]] = i
        for j in range(len(nums)):
            ans[j] = dic[nums[j]]
            
        return ans

        