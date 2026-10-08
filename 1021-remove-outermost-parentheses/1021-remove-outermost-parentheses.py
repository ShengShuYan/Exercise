class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        dif = 0
        ans = []
        for c in s:
            if c == ')':
                dif -= 1
                if dif > 0:
                   ans.append(c) 
            else:
                dif += 1
                if dif > 1:
                    ans.append(c)

        return ''.join(ans)
        