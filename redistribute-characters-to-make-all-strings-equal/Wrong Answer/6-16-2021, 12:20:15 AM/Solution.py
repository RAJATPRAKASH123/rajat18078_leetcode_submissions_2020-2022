// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        arr = [0]*26
        for word in words:
            for i in word:
                arr[ord(i)-97] += 1
        for i in arr:
            if i != 0 and i%len(arr) != 0:
                return False
        return True