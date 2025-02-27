// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        arr = []
        ans = 0
        cur = 0
        for i in s:
            ans = max(ans, cur)
            if not arr:
                arr.append(i)
                continue
            if arr[-1] == '(' and i == ')':
                cur += 2
                arr.pop()
                continue
            if i == ')':
                cur = 0
                arr =[]
            arr.append(i)
        ans = max(ans, cur)
        return ans