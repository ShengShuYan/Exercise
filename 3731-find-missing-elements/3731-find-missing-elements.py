class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        n = nums[-1]
        sm = nums[0] + 1
        start = 1
        for i in range(sm, n):
            if nums[start] == i:
                start += 1
            else:
                ans.append(i)

        return ans

        