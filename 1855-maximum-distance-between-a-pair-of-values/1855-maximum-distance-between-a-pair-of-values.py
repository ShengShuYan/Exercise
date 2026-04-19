from bisect import bisect_right
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        l = min(l1, l2)
        dis = 0
        nums2 = [-x for x in nums2]
        for i in range(l):
            v1 = -nums1[i]
            v2 = nums2[i]
            if v1<v2:
                continue
            j = bisect_right(nums2, v1) - 1
            dis = max(j - i, dis)
            # j = l2-1
            # while j > i + dis:
            #     if nums2[j] >= v1:
            #         dis = j-i
            #         break
            #     j -= 1
            if dis > l2 - i:
                break
        return dis


        