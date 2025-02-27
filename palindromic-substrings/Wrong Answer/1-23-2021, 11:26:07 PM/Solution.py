// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        arr=list(s)
        # yeah
        temp = 0
        vis = []
        dp=[[-1 for i in range(n+3)] for j in range(n+3)]
        
        def helper(arr,i,j, count):
            
            nonlocal temp,vis
            if count > 0:
                print([i,j],count)
                if i == j and [i,j] not in vis:
                    temp += count
                    vis+=[[i,j]]
                elif i-j == 1 and [i,j] not in vis:
                    temp += count
                    vis+=[[i,j]]
            if i >= j:
                return
            if dp[i][j] != -1:
                return dp[i][j]
            if arr[i] == arr[j]:
                helper(arr,i+1,j-1, count+1)
            helper(arr,i,j-1, 0)
            helper(arr,i+1,j, 0)
        helper(arr,0, len(arr)-1,0)
        return temp+len(arr)