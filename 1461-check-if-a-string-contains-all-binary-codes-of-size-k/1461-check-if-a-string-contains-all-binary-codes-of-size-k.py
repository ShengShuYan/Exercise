class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = 2 ** k
        len_s = len(s)
        if len_s <  k:
            return False
        subset = set()
        for j in range(len_s - k + 1):
            subset.add(s[j: j+k])

        for i in range(n):
            sub = bin(i)[2:].zfill(k)
            if sub not in subset:
                return False

        return True