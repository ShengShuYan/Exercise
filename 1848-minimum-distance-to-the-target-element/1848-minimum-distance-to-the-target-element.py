class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = len(nums)
        dif = 0
        maxd = max(start, l - start - 1)
        while dif <= maxd:
            left = start - dif
            right = start + dif
            if left >= 0 and nums[left] == target:
                return dif
            if right < l and nums[right] == target:
                return dif
            dif += 1



        