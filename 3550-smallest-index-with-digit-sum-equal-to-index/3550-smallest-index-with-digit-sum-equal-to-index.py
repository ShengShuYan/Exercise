class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if sum(map(int, str(v))) == i:
                return i

        return -1

        