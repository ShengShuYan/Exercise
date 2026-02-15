class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)
        l = []
        cin = 0

        if n1 > n2:
            b = '0' * (n1-n2) + b
        else:
            a = '0' * (n2 - n1) + a
            n1 = n2
        for i in range(-1, -n1-1, -1):
            cur = int(a[i]) + int(b[i]) + cin
            if cur > 1:
                l.append(str(cur%2))
                cin = 1
            else:
                l.append(str(cur%2))
                cin = 0

        if cin == 1:
            l.append(str(cin))

        l.reverse()

        return ''.join(l)

            

            