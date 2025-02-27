// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # But, let's first try O(nlogn), nahhh its easy
        res = [0]*(n+1)
        
        # This question is not straightforward : I saw the soln
        # Here, we need to check the least significant bit
        for i in range(1, n+1):
            res[i] = res[i & (i-1)] + 1
        return res
                 
        # So, we have to count no. of bits in O(n) and single pass
        
'''
0    : i
1    : i & (i-1) = 0
10   : 0
11   : 
100  :
101  :
110
111
1000
'''