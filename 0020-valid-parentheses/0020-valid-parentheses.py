class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for c in s:
            if c in '({[':
                ans.append(c)
            else:
                if not ans:
                    return False
                lat = ans.pop()
                if c == ')' and lat == '(':
                    continue
                elif c == '}' and lat == '{':
                    continue
                elif c == ']' and lat == '[':
                    continue
                return False
        return False if ans else True


        