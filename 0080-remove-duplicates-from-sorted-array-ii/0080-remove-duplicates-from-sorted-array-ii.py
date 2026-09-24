class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        j = 1
        d = float('inf')
        l = len(nums)
        while j < l:
            v = nums[j]
            if v == d:
                j += 1
                continue
            if v != nums[i-1]:
                d = float('inf')
            else:
                d = v
            nums[i] = v
            i += 1
            j += 1

        return i



        