class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == val:
                while r > 0 and nums[r] == val:
                    nums.pop()
                    r -= 1
                if l > r:
                    break
                nums[l] = nums[r]
                nums.pop()
                r -= 1
            l += 1
        return r + 1

        