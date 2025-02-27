// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp = ""
        temp2 = ""
        for i in word1:
            temp += i
        for j in word2:
            temp2 += j
        return temp == temp2