class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = 2 ** k
        len_s = len(s)
        if len_s <  k:
            return False

        subset = set()
        mask = (1 << k) - 1

        cur = 0
        
        for z in range(k):
            cur = (cur << 1) | (ord(s[z]) - 48)

        subset.add(cur)

        for j in range(k, len_s):
            cur = ((cur << 1) & mask) | (ord(s[j]) - 48)
            subset.add(cur)

        if len(subset) == n:
            return True
            
        return False     