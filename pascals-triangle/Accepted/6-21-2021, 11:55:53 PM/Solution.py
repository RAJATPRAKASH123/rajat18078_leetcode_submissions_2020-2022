// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            cur = [0] * (len(res)+1)
            for j in range(len(cur)):
                if j == 0 :
                    cur[j] = res[-1][0]
                elif j == len(cur)-1:
                    cur[j] = res[-1][-1]
                else:
                    cur[j] = res[-1][j-1] + res[-1][j]
            res.append(cur[:])
        return res