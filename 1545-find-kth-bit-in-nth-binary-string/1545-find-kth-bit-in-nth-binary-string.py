class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        n0 = 1
        sub1 = '0'
        while n0 < n:
            sub1 = self.form(sub1)
            n0 += 1

        return sub1[k-1]


    def form(self, sub):
        isub = ''.join('1' if c == '0' else '0' for c in sub)
        rsub = isub[::-1]
        return sub + '1' + rsub

        

        