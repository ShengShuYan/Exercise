class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append('(')
            else:
                if not stack:
                    return error
                else:
                    fore = stack.pop()
                    if fore == '(':
                        stack.append(1)
                    else:
                        cur = fore
                        while stack:
                            fore = stack.pop()
                            if fore == '(':
                                stack.append(2*cur)
                                break
                            else:
                                cur += fore
        return sum(stack)
