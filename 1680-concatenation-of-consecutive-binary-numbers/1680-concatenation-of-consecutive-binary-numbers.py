class Solution:
    def concatenatedBinary(self, n: int) -> int:
        r = 0
        for i in range(1, n+1):
            l = i.bit_length()
            r = ((r << l) | i) % (10**9 + 7)
        return r % (10**9 + 7)
            

        