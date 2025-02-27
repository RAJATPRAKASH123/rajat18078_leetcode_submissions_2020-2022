// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        # if len(s) == 1 and s in wordDict:
        #     return [s]
        ans = []
        n = len(s)
        dp = [[-1 for i in range(n+1)] for j in range(n+1)]
        def helper(s, i, cur):
            nonlocal ans
            if i >= n:
                ans += [cur[:-1]]
                # print("inside")
                return True

            temp = False
            for k in range(i, n): 
                # print(s[i:k+1])
                temp = temp or ((s[i:k+1] in wordDict) and helper(s, k+1, cur + s[i:k+1] + " "))
            
        cur = ""
        helper(s,0, cur)
        return ans