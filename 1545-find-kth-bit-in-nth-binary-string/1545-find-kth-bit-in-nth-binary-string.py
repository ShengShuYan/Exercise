class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        mid = 1 << (n-1)
        if k == mid:
            return '1'

        if k < mid:
            return self.findKthBit(n-1, k)

        mir = 1 << n - k
        ans = self.findKthBit(n-1, mirror)
        return '1' if ans == '0' else '0' 
        
        

        