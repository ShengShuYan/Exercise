class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        dif = 0
        stack = []
        ans = []
        for c in s:
            if c == ')':
                dif -= 1
                stack.append(')')
            else:
                dif += 1
                stack.append('(')
            if dif == 0:
                ans += stack[1:-1]
                stack = []

        return ''.join(ans)
        