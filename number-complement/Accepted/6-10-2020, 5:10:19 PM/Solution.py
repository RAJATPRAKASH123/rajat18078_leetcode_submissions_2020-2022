// https://leetcode.com/problems/number-complement

class Solution:
    def findComplement(self, num: int) -> int: 
        ans=0
        c =0
        s = str(bin(num))[2:]
        for i in s[::-1]:
            if i == '0':
                ans += 2**c
            c += 1
        return ans