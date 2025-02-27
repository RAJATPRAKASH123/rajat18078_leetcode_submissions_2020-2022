// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                s = stack.pop()
                f= stack.pop()
                stack.append(f+s)
            elif i == "-":
                s = stack.pop()
                f = stack.pop()
                stack.append(f-s)
            elif i == "/":
                s = stack.pop()
                f = stack.pop()
                res = f/s
                if res > 0:
                    res = f//s
                else:
                    res = math.ceil(f/s)
                stack.append(res)
            elif i == "*":
                s = stack.pop()
                f = stack.pop()
                stack.append(f*s)
            else:
                stack.append(int(i))
        return stack[-1]