class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = sorted(nums)
        a = 0
        b = len(nums)
        while a < b and (L[a] == nums[a]):
            a += 1
        if a == b - 1:
            return 0
        while b > a and (L[b-1] == nums[b-1]):
            b -= 1 
        return b - a

        