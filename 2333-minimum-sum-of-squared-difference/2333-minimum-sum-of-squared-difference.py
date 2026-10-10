class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        l = len(nums1)
        for i in range(l):
            nums2[i] = abs(nums2[i]-nums1[i])
        nums2.sort(reverse=True)
        j = k1+k2
        ind = 0
        while ind<l and j > 0:
            v = nums2[ind]
            if v == 0:
                return 0
            if ind == l-1:
                if l * v <= j:
                    return 0
                else:
                    v1 = v - j // l
                    u2 = j % l
                    return (v1-1)**2*u2 + v1**2*(l-u2)
            vpos = nums2[ind+1]
            if (ind+1) * (v-vpos) < j:
                    j -= (ind+1) * (v-vpos)
                    ind += 1
            else:
                v1 = v - j // (ind+1)
                u2 = j % (ind+1)
                return (v1-1)**2*u2 + v1**2*(ind+1-u2) + sum(x**2 for x in nums2[ind+1:])
        return sum(x**2 for x in nums2)