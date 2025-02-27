// https://leetcode.com/problems/repeated-dna-sequences

from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        arr = defaultdict(int)
        
        for i in range(len(s)-9):
            arr[s[i:i+10]] += 1
        res = []
        for pattern in arr:
            if arr[pattern] > 1:
                res.append(pattern)
        return res