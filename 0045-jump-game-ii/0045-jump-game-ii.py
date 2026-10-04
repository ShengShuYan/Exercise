class Solution:
    def jump(self, nums: list[int]) -> int:
        tar = len(nums)
        dq = [float('inf')] * tar
        dq[tar-1] = 0
        i = tar - 2
        while i >= 0:
            v = nums[i]
            if i + v >= tar:
                dq[i] = 1
            else:
                dq[i] = min(dq[i:i+v+1])+1
            i -= 1
        return dq[0]
        