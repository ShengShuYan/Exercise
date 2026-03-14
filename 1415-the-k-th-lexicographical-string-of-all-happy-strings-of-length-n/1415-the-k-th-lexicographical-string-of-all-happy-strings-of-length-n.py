class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        N = 2 ** (n-1)
        if k > 3 * N or n == 0:
            return ''

        ans = []
        base = ['a', 'b', 'c']

        cur = (k-1) // N

        ans.append(base[cur])
        k = (k-1) % N
        N = N // 2

        for _ in range(n-1):
            move = k//N
            if cur == 0:
                if move == 0:
                    cur = 1
                else:
                    cur = 2
            elif cur == 1:
                if move == 0:
                    cur = 0
                else:
                    cur = 2
            else:
                if move == 0:
                    cur = 0
                else:
                    cur = 1
            
            ans.append(base[cur])           
            k = k % N
            N = N // 2

        return ''.join(ans)
