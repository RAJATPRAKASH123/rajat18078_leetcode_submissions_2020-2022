// https://leetcode.com/problems/word-break

from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # charsInStr = set(s)
        # charsInDict = set()
        # for word in wordDict:
        #     for i in word:
        #         charsInDict.add(i)
        # if charsInStr - charsInDict:
        #     return False
        memo = defaultdict(bool)
        def checkIt(s, start=0):
            if start in memo:
                return memo[start]
            if start == len(s):
                return True
            found = False
            for word in wordDict:
                if len(word) > len(s)-start or word != s[start:start+len(word)]:
                    continue
                found = found or checkIt(s, start + len(word))
            memo[start] = found
            return found
        return checkIt(s)