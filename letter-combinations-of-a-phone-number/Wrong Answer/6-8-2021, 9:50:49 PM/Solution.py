// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits = list(digits)
        poss = ["","", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def helper(start, cur=""):
            if start == len(digits):
                res.append(cur[:])
                return
            for letter in poss[int(digits[start])]:
                helper(start+1, cur + letter)
        helper(0 )
        return res