from collections import deque

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        queue = deque()

        for i in range(len(nums)-1, -1, -1):
            val = nums[i]
            while val > 0:
                dig = val % 10
                queue.appendleft(dig)
                val = val//10
        return list(queue)


        