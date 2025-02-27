// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        arr = list(s)
        if s.count('00') > 0:
            return 0
        if s[0] == '0':
            return 0
	        
        for i in range(1,len(s)):
            if s[i] == '0' and int(s[i-1]) > 2:
                return 0
        dp = [-1 for i in range(len(s))]
        def helper(arr, i):
            temp = 0
            if i == -1:
                return 1
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i] 
            if arr[i] == '0':
                return helper(arr,i-2)
            temp +=  helper(arr, i-1)
            if arr[i-1] == '1':
                temp += helper(arr, i-2)
            if arr[i-1] == '2' and int(arr[i]) <= 6:
                temp += helper(arr, i-2)
            dp[i] = temp 
            return temp
        return helper(arr,len(arr)-1)