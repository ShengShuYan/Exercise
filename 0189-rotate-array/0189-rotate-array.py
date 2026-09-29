class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        m = k % l
        L = nums[l-m:]
        del nums[l-m:]
        nums[0:0] = L
        return nums