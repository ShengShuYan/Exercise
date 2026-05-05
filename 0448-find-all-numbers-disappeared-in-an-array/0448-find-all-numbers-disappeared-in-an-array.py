class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (1+n)
        for i in nums:
            count[i] = 1
        return [i for i in range(1, 1+n) if count[i] == 0]


        