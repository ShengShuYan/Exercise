class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        dif = 0
        ans = 0
        for c in s:
            if c == ')':
                dif -= 1
                if dif < 0:
                    ans += 1
                    dif = 0
            else:
                dif += 1
        return ans + dif