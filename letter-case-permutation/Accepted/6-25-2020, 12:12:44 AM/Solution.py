// https://leetcode.com/problems/letter-case-permutation

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        arr = []
        def helper(s, temp):
            nonlocal arr
            if not s:
                arr.append(temp)
                # print(temp)
                return 
            i = s[0]
            if i.isdigit():
                helper(s[1:], temp+i )
            else:
                helper(s[1:], temp + i.lower())
                helper(s[1:], temp + i.upper())

        helper(s, "")
        return arr