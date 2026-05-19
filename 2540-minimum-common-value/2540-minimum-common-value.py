class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        i1, i2 = 0, 0
        while i1 < l1 and i2 < l2:
            v1, v2 = nums1[i1], nums2[i2]
            if v1 == v2:
                return v1
            if v1 < v2:
                i1 += 1
            else:
                i2 += 1

        return -1
        