// https://leetcode.com/problems/count-square-submatrices-with-all-ones

class Solution:
    def countSquares(self, arr: List[List[int]]) -> int:
        n = len(arr)
        m = len(arr[0])
        hor = [[0 for i in range(m+1)] for j in range(n+1)]
        b_sum = [[0 for i in range(m+1)] for j in range(n+1)]
        for j in range(1,m+1):
            for i in range(1,n+1):
                hor[i][j] = hor[i-1][j] + arr[i-1][j-1]
        for j in range(1,m+1):
            for i in range(1,n+1):
                b_sum[i][j] = hor[i-1][j] + b_sum[i][j-1] + arr[i-1][j-1]
        # return b_sum
        count = 0
        for k in range(1, min(m+1,n+1)):
            flag = False
            for j in range(1,m+1):
                for i in range(1,n+1):
                    l,u = i-k, j-k
                    if i-k < 0:
                        l = 0
                    if j-k < 0:
                        u = 0
                    tt = b_sum[i][j] - b_sum[l][j] - b_sum[i][u] + b_sum[l][u]
                    if tt == k**2:
                        flag = True
                        count += 1
            if not flag:
                break
        return count
'''

return 



'''