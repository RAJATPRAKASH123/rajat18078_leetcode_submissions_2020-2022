// https://leetcode.com/problems/number-of-matching-subsequences

class Solution:
    def numMatchingSubseq(self, s: str, arr: List[str]) -> int:
        
        for i in s:
            for j in range(len(arr)):
                if len(arr[j]) == 0:
                    continue
                if arr[j][0] == i:
                    arr[j] = arr[j][1:]
        # return arr
        return arr.count("")