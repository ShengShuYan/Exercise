class Solution:
    def minInsertions(self, s: str) -> int:
        dif = 0
        ans = 0
        i = 0
        l = len(s)
        while i < l:
            v = s[i]
            if v == '(':
                dif += 1
            elif i<l-1 and s[i+1] == ')':
                dif -= 1
                i += 1
            else:
                ans += 1
                dif -= 1
            i += 1
            if dif < 0:
                ans += 1
                dif = 0

        return ans + 2*dif

            
                


        