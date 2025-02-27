// https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows==1:
            return s
        res = ""
        for row in range(numRows):
            cur = ""
            if row == 0:
                cur = s[0::2*(numRows-1)]
            elif row == numRows-1:
                cur = s[numRows-1::2*(numRows-1)]
            else:
                for j in range(row, len(s), 2*(numRows-1)):
                    middle = ""
                    if j + 2*(numRows - row - 1) < len(s):
                        middle = s[j + 2*(numRows - row - 1)]
                    cur += s[j] + middle
            # print(cur)
            res += cur
            
        return res
"""
"PAHN
 AYLIIRGYAILRIPSI"
"""