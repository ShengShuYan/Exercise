class Solution:
    def binaryGap(self, n: int) -> int:
        c = bin(n)

        i = 2
        while c[i] != '1':
            i += 1
            if i == len(c):
                return 0

        j = i + 1
        dis = 0
        while j < len(c):
            if c[j] == '1':
                dis = max(dis, j - i)
                i = j
            j += 1

        return dis or 0