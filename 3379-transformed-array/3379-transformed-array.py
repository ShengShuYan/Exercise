class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        L = len(nums)
        for i, c in enumerate(nums):
            if c != 0:
                result.append(nums[(i + c) % L])
            else:
                result.append(0)
        return result