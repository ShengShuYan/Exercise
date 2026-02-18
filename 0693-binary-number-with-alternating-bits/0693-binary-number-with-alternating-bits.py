class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b_n = iter(str(bin(n)[2:]))
        pre = next(b_n)

        for t in b_n:
            if pre == t:
                return False
            else:
                pre = t

        return True

        