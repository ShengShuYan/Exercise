class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        mis = 0
        rem = [0] * len(nums)
        for i in nums:
            rem[i-1] += 1
        for j in range(len(rem)):
            if rem[j] == 0:
                mis = j+1
            elif rem[j] == 2:
                dup = j+1
            if mis and dup:
                break
        return [dup, mis]



        