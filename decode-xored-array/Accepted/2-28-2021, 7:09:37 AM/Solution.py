// https://leetcode.com/problems/decode-xored-array

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l_encoded = len(encoded)
        res = [0 for i in range( l_encoded +1 )]
        res[0] = first
        for i in range(l_encoded):
            res[i+1] = encoded[i]^first
            first = res[i+1]
        return res