class Solution:
    def jump(self, nums: list[int]) -> int:
        l = len(nums)
        if l <= 1:
            return 0
        jumps = 0
        cur_end = 0
        far = 0

        for i in range(l-1):
            far = max(far, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = far

                if cur_end >= l-1:
                    return jumps
        return jumps