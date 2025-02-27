// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque([])
        idx = 0
        for i in s:
            if not stack:
                stack.append([i, idx])
                idx += 1
                continue
            if i == '(':
                stack.append([i, idx])
            elif i == ')':
                if stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            idx += 1
        
        # print(stack)
        res = 0
        for i in range(len(stack)):
            if i == 0:
                res = max(res, stack[i][1])
                continue
            res = max(res, stack[i][1] - stack[i-1][1])
        res = max(res, len(s) - stack[-1][1]- 1)
        print(stack)
        return res