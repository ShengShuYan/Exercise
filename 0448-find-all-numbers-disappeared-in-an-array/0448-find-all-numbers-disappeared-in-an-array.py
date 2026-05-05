class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n
        for i in nums:
            count[i-1] += 1
        return [i+1 for i in range(n) if count[i] == 0]


        