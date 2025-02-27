// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            if i in [')', '}', ']']:
                if not stack:
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                if i == '}' and stack[-1] == '{':
                    stack.pop()
                if i == ']' and stack[-1] == '[':
                    stack.pop()
        return len(stack) == 0