# 6 * log2 10 = 6 * 3.32192809489 < 20
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        p_set = {2, 3, 5, 7, 11, 13, 17, 19}
        for i in range(left, right + 1):
            count += int(bin(i).count('1') in p_set)

        return count

