import heapq
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            nums.extend(row)
        judge= nums[0] % x
        for item in nums:
            if item % x != judge:
                return -1
        
        nums.sort()

        mid = nums[len(nums) // 2]

        return sum([abs(item - mid)//x for item in nums])


        