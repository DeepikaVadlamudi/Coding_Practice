class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*", "/"}
        stack = []
        ans = 0
        for i in tokens:
            if i in operators:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    ans = (a+b)
                elif i == "-":
                    ans = (a-b)
                elif i == "*":
                    ans = (a*b)
                elif i == "/":
                    ans = int(a/b)
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack[-1]
                    
