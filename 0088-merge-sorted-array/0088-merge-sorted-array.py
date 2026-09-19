class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m-1
        j = n-1
        r = m+n-1
        while i>=0 and j>=0:
            v1 = nums1[i]
            v2 = nums2[j]
            if v2 > v1:
                nums1[r] = v2
                j -= 1
            else:
                nums1[r] = v1
                i -= 1
            r -= 1
        while j >= 0:
            nums1[r] = nums2[j]
            r -= 1
            j -= 1



        