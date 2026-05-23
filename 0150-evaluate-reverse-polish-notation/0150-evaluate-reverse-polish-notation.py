class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop()+stack.pop())
            elif c == "-":
                stack.append(-stack.pop()+stack.pop())
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                i2 = stack.pop()
                i1 = stack.pop()
                stack.append(int(i1/i2))
            else:
                stack.append(int(c))

        return stack[0]