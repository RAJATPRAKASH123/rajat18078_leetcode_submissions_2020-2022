// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp = ""
        temp2 = ""
        for i,j in zip(word1, word2):
            temp += i
            temp2 += j
        return temp == temp2