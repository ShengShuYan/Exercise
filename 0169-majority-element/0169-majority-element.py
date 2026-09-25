from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        tar = n // 2
        c = Counter(nums)
        for v, tim in c.items():
            if tim > tar:
                return v       
        