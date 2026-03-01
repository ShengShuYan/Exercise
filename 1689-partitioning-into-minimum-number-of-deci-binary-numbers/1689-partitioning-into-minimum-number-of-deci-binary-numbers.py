class Solution:
    def minPartitions(self, n: str) -> int:
        ini = 0
        for c in n:
            if c == '1':
                cur = 1
            elif c == '2':
                cur = 2
            elif c == '3':
                cur = 3
            elif c == '4':
                cur = 4
            elif c == '5':
                cur = 5
            elif c == '6':
                cur = 6
            elif c == '7':
                cur = 7
            elif c == '8':
                cur = 8
            elif c == '9':
                cur = 9

            if cur > ini:
                ini = cur

        return ini
            
        