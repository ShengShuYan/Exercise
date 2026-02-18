class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b_n = str(bin(n)[2:])
        pre = b_n[0]
        for c in b_n[1:]:
            if c == pre:
                return False
            else:
                pre = c

        return True

        