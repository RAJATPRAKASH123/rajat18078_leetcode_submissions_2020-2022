// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def checkIt(s, start=0):
            if start == len(s):
                return True
            found = False
            for word in wordDict:
                if len(word) > len(s)-start or word != s[start:start+len(word)]:
                    continue
                found = found or checkIt(s, start + len(word))
            return found
        return checkIt(s)