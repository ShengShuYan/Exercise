class Solution:
    def sumAndMultiply(self, n: int) -> int:
        L = []
        N = str(n)
        for digit in N:
            if digit != '0':
                L.append(digit)

        if not L:
            x = 0
        else:
            x = int(''.join(L))

        return x * sum(int(x) for x in L)
        