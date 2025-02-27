// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if stack and s[stack[-1]] == '(' and s[i] == ')':
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        if not stack:
            return len(s)
        maxm = 0
        start = 0
        for i in stack:
            maxm = max(maxm, i - start - 1)
            start = i
            
        maxm = max(maxm, len(s) - 1 - stack[-1])
        return maxm
'''
stack

(
)

'''