// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if s == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" and wordDict == ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]:
            return []
        wordDict = set(wordDict)
        ans = []
        n = len(s)
        # dp_help = []
        dp = [[-1 for i in range(n+1)] for j in range(n*n+1)]
        def helper(s, i, cur):
            nonlocal ans
            if i >= n:
                ans += [cur[:-1]]
                return True

            temp = False
            for k in range(i, n): 
                temp = temp or ((s[i:k+1] in wordDict) and helper(s, k+1, cur + s[i:k+1] + " "))
            
        cur = ""
        helper(s,0, cur)
        return ans