// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        # s = [int(i) for i in s]
        s = list(s)
        def helper(s):
            # given
            nonlocal a, b
            # checking whether visited or not
            if "".join(s) in visited:
                return
            
            visited.add("".join(s))
            temp_s = s[::]
            for i in range(len(s)):
                if i % 2 == 1:
                    s[i] = str((int(s[i]) + a) % 10)
            s_add = s[::]
            s = temp_s
            s =   s[len(s)-b:] + s[:len(s)-b]
            s_rotate = s[::]
            
            helper(s_add)
            helper(s_rotate)
        helper(s)
        # print(visited)
        return min(visited)