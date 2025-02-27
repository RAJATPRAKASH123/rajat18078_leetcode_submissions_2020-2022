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
        
        for i in range(1, len(stack)):
            maxm = max(maxm, stack[i] - stack[i-1])
        return max(maxm, stack[0], len(s) - 1 - stack[-1])
'''
stack

(
)

'''