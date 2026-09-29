class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        nums1 = nums[:]
        l = len(nums)
        m = k % l
        for i in range(l):
            n = (i + m) % l
            nums[n] = nums1[i]
        return nums