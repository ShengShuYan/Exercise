from collections import deque

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num > 9:
                for dig in str(num):
                    ans.append(int(dig))
            else:
                ans.append(num)

        return ans

        