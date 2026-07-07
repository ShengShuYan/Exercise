class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        L = []
        N = str(n)
        for digit in N:
            if digit != '0':
                L.append(digit)

        x = int(''.join(L))

        return x * sum(int(x) for x in L)
        