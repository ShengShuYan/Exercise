from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = None
        v = 0
        for num in nums:
            if v == 0:
                c = num
            if num == c:
                v += 1
            else:
                v -= 1
        return c
            