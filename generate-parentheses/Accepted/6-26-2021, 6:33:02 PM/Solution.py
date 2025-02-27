// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def parenth(left , right , stack = []):
            
            nonlocal n

            if len(stack) == 2*n:
                res.append("".join(stack)) 
                return
            
            if left < n:
                stack.append('(')
                parenth(left+1, right)
                stack.pop()
            if left > right:
                stack.append(')')
                parenth(left, right+1)
                stack.pop()
            
            
            
        parenth(0, 0)
        return res
                 
'''

'''