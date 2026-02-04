class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return True
        elif nums[0]>nums[-1]:
            for i in range(n-1):
                if nums[i] < nums[i+1]:
                    return False
            return True
        elif nums[0] < nums[-1]:
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    return False
            return True
        else:
            for z in range(n-1):
                if nums[z] != nums[z+1]:
                    return False
            return True