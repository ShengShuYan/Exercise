class Solution:
    def _eval_top(self, op_stack: list, num_stack: list) -> None:
        op = op_stack.pop()
        B = num_stack.pop()
        A = num_stack.pop()
        
        if op == ',':
            num_stack.append(A | B)
        elif op == '*':
            res = set()
            for a in A:
                for b in B:
                    res.add(a + b)
            num_stack.append(res)

    def braceExpansionII(self, expression: str) -> list[str]:
        num_stack = []
        op_stack = []
        
        i = 0
        n = len(expression)
        
        while i < n:
            c = expression[i]
            
            if c.isalpha():
                if i > 0 and expression[i-1] == '}':
                    op_stack.append('*')
                
                word = ""
                while i < n and expression[i].isalpha():
                    word += expression[i]
                    i += 1
                num_stack.append({word})
                continue
                
            elif c == '{':
                if i > 0 and (expression[i-1] == '}' or expression[i-1].isalpha()):
                    op_stack.append('*')
                op_stack.append('{')
                
            elif c == ',':
                while op_stack and op_stack[-1] == '*':
                    self._eval_top(op_stack, num_stack)
                op_stack.append(',')
                
            elif c == '}':
                while op_stack and op_stack[-1] != '{':
                    self._eval_top(op_stack, num_stack)
                op_stack.pop()
            i += 1
            
        while op_stack:
            self._eval_top(op_stack, num_stack)
            
        return sorted(list(num_stack[0]))
