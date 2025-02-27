// https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur_perids = 0
        path = path.split("""/""")
        res = ""
        
        for i in path:
            if not i or i == '.':
                continue
            if i != '..':
                stack.append(i)
                continue
            if stack:
                stack.pop()
        for i in stack:
            res = res + '/' + i
        if not res:
            return '/'
        return res