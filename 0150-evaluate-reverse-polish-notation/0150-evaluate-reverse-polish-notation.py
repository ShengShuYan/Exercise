class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+', "-", "*", "/"}
        stack = []

        for c in tokens:
            if c not in op:
                stack.append(int(c))
            else:
                i2 = stack.pop()
                i1 = stack.pop()
                if c == "+":
                    stack.append(i1+i2)
                elif c == "-":
                    stack.append(i1-i2)
                elif c == "*":
                    stack.append(i1*i2)
                else:
                    stack.append(int(i1/i2))

        return stack[0]