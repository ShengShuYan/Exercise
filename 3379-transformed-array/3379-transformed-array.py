class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        L = len(nums)
        for i in range(L):
            if nums[i] > 0:
                ind = (i + nums[i]) % L
                result.append(nums[ind])
            elif nums[i] < 0:
                ind = (i + nums[i]) % L
                result.append(nums[ind])
            else:
                result.append(nums[i])
        return result