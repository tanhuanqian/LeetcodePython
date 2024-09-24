class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c in ('+', '-', '*', '/'):
                n1 = stack.pop()
                n2 = stack.pop()
                if c == '+':
                    stack.append(n1+n2)
                elif c == '-':
                    stack.append(n2-n1)
                elif c == '*':
                    stack.append(n2*n1)
                elif c == '/':
                    result = n2 / n1
                    if result > 0:
                        stack.append(int(result))
                    else:
                        stack.append(round(result))
            else:
                temp = int(c)
                stack.append(temp)
        return stack[-1]    

string = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
print(solution.evalRPN(string))