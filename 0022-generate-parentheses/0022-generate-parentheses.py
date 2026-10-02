class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = [['(', 1, n-1]]
        for i in range(2*n-1):
            cur = []
            while ans:
                x = ans.pop()
                if x[2] >= 1:
                    cur.append([x[0]+'(', x[1]+1, x[2]-1])
                if x[1] >= 1:
                    cur.append([x[0]+')', x[1]-1, x[2]])
            ans = cur
        return [x[0] for x in ans]

                    


        