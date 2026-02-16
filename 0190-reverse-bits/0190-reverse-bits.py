class Solution:
    def reverseBits(self, n: int) -> int:
        to_32bit = lambda n: format(n & 0xFFFFFFFF, '032b')
        n = str(to_32bit(n))[::-1]
        return int(n, base = 2)
            

        