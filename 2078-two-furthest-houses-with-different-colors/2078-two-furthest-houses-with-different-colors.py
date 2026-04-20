
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        L = len(colors)
        vi = colors[0]
        vf = colors[-1]
        if vi != vf:
            return L - 1
        i = 1
        while i < L and colors[i] == vf:
            i += 1
        f = L - 2
        a1 = L - 1 - i
        while f > -1 and colors[f] == vi:
            f-=1
        return max(a1, f)