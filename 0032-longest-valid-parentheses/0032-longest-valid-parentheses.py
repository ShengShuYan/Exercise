class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        ans = 0
        if l < 2: return 0
        stack = [-1]
        for i in range(l):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans       
