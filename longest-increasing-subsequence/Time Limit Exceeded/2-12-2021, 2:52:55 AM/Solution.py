// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        arr.append(10000000000)
        n = len(arr)
        
        # Recursive function
        dp = [[-1 for j in range(n+1)] for i in range(n+1)]
        
        
        
        def helper(i, nextt):
            if i == -1:
                return 0
            if dp[i][nextt] != -1:
                return dp[i][nextt]

            prev = -1
            for t in range(i, -1, -1):
                if arr[t] < arr[nextt]:
                    prev = t
                    break
            if prev == -1:
                return 0
            dp[i][nextt] = max(1 + helper(t-1, t ), helper( t-1, nextt) )
            return dp[i][nextt]
            
        return helper(n-2, n-1) 