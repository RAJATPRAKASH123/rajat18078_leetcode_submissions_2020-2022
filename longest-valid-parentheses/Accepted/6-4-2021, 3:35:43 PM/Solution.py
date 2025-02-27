// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, par in enumerate(s):
            if not stack or stack[-1][0] == ')' or par == '(':
                stack.append([par, i])
                continue
            stack.pop()
        if not stack:
            return len(s)
        res = 0
        # print(stack)
        for i in range(1, len(stack)):
            res = max(res, stack[i][1]-stack[i-1][1]-1)
        res = max(res, len(s)-stack[-1][1]-1, stack[0][1])
        return res