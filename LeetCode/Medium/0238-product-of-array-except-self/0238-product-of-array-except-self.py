class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L= len(nums)
        l = [1]
        for i in range(1, L):
            l.append(l[i-1] * nums[i-1])
        R = 1
        for i in range(L-1, -1, -1):
            l[i] *= R
            R *= nums[i]
        return l
        




