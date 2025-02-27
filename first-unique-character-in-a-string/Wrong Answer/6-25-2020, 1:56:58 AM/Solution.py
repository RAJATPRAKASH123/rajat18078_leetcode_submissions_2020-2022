// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = dict()
        count = 0
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0
        papa = True
        for i in s:
            if i in hm.keys():
                if hm[i] - 1 >= 0:
                    return hm[i] - 1
                    break
                papa = False
            hm[i] = count
            count += 1
        if papa:
            return 0
        return -1