// https://leetcode.com/problems/count-sorted-vowel-strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[-1 for i in range(5)] for j in range(n+2)]
        
        def helper(vowels, n, s):
            
            if n == 0:
                return 1
            temp = 0
            
            for i in vowels:
                if ord(i) >= ord(s):
                    if dp[n][vowels.index(i)] != -1:
                        return dp[n][vowels.index(i)] 
                    temp += helper(vowels, n-1, i)
                    if s in vowels:
                        dp[n][vowels.index(s)] = temp
            return temp
        return helper(['a','e','i','o','u'], n, 'A')
'''
arr, n
for i in 
return helper(arr, )
'''