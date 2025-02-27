// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        opening_brackets = ('(', '{', '[')
        closing_brackets = (')', '}', ']')
        while i < len(s):
            if s[i] in opening_brackets:
                stack.append(s[i])
                i += 1
                continue
            if not stack:
                return False
            if stack and (stack[-1] == '(' and (s[i] == ')') or (stack[-1] == '{' and s[i] == '}') or (stack[-1] == '[' and s[i] == ']')) :
                stack.pop()
            i += 1
        if stack:
            return False
        return True