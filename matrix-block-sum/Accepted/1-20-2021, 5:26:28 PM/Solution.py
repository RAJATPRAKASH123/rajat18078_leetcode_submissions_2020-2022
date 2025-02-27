// https://leetcode.com/problems/matrix-block-sum

class Solution:
    def matrixBlockSum(self, arr: List[List[int]], k: int) -> List[List[int]]:
        n = len(arr)
        m = len(arr[0])
        # ver = [[ 0 for i in range(m+1)] for j in range(n+1)]
        hor = [[ 0 for i in range(m+1)] for j in range(n+1)]
        ans = [[ 0 for i in range(m)] for j in range(n)]
        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         ver[i][j] = ver[i][j-1] + arr[i-1][j-1]
        block_sum = [[ 0 for i in range(m+1)] for j in range(n+1)]
        for j in range(1,m+1):
            for i in range(1,n+1):
                hor[i][j] = hor[i-1][j] + arr[i-1][j-1]
                block_sum[i][j] = hor[i-1][j] + block_sum[i][j-1] + arr[i-1][j-1]
        # return block_sum
        
        for j in range(m):
            for i in range(n):
                
                r,l,u,d = i+k, i-k, j-k, j+k
                
                if i+k >= n:
                    r = n-1
                if i-k < 0:
                    l = 0
                if j+k >= m:
                    d = m-1
                if j-k < 0:
                    u = 0
                ans[i][j] = block_sum[r+1][d+1] + block_sum[l][u] - block_sum[r+1][u] - block_sum[l][d+1]
        return ans
        
#         for i in range(n):
#             for j in range(m):
                
#                 r,l,u,d = i+k,i-k,j-k,j+k
#                 if i+k >= n:
#                     r = n-1
#                 if i-k < 0:
#                     l = 0
#                 if j+k >= m:
#                     d = m-1
#                 if j-k < 0:
#                     u = 0
                
#                 ans[i][j] = hor[r+1][j+1]-hor[l][j+1] + ver[i+1][d+1] - ver[i+1][u] - arr[i][j]
#         print(hor, ver)
        