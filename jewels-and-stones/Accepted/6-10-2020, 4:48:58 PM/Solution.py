// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c=0
        for i in J:
            for j in S:
                if i == j:
                    c +=1
        return c
    