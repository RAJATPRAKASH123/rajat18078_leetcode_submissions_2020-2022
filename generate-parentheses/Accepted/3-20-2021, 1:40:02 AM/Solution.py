// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def helper(n, left, right, ans=""):
            if left == n and right == n:
                res.append(ans)
            if left > right and left < n:
                helper(n, left+1, right, ans + '(' )
                helper(n, left, right+1, ans + ')' )
            elif left == right and left < n:
                helper(n, left+1, right, ans + '(' )
            elif left == n:
                res.append(ans + (n-right)*')')
        
        helper(n, 0, 0)
        return res