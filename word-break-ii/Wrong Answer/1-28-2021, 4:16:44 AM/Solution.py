// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        if len(s) == 1 and s in wordDict:
            return [s]
        ans = []
        n = len(s)
        # dp
        def helper(s, i, cur):
            nonlocal ans
            if i >= n:
                ans += [cur]
                return True
            temp = False
            for k in range(i+1, n): 
                temp = temp or ((s[i:k+1] in wordDict) and helper(s, k+1, cur + [[i,k+1]]))
            
        cur = []
        helper(s,0, cur)
        # print(ans)
        fina = []
        for i in ans:
            temp = ""
            for j in i:
                temp += s[j[0]:j[1]] + " "
            # print(temp)
            fina += [temp[:-1]]
        return fina