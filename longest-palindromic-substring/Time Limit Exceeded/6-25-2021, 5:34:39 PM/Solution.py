// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
          
          # Recursive Solution
#         n = len(s)
#         dp = [[-1 for j in range(n)] for i in range(n)]
#         start, end = 0, 0
#         def lps(i, j):
#             if dp[i][j] != -1:
#                 return dp[i][j]
#             nonlocal start, end
#             if i == j:
#                 dp[i][j] = True
#                 return True
#             if i + 1 == j:
#                 if s[i] == s[j] and (j-i > end - start):
#                     start = i ; end = j
#                     dp[i][j] = True
#                 return s[i] == s[j]
#             if s[i] == s[j] and lps(i+1, j-1):
#                 if (j-i > end - start):
#                     start = i ; end = j
#                 dp[i][j] = True
#                 return True    
#             lps(i+1, j)
#             lps(i, j-1)
#             dp[i][j] = False
            
#         lps(0, len(s)-1)
#         return s[start:end+1]
        n = len(s)
        dp = [[True if i == j else False for i in range(n)] for j in range(n)]
        start, end = 0, 0
        for j in range(1, n):
            for i in range(j-1,-1, -1):
                if j - i <= 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j] and end - start < j - i:
                    start, end = i, j
        return s[start:end+1]
                    
'''
s : return longest palindromic substring

for each i , I will check update max using two types of palindromes
1. odd length
2. even length

"babad"

'''