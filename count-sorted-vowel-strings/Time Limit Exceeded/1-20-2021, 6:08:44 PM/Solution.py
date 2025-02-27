// https://leetcode.com/problems/count-sorted-vowel-strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def helper(vowels, n, s):
            
            if n == 0:
                return 1
            temp = 0
            for i in vowels:
                if ord(i) >= ord(s):
                    temp += helper(vowels, n-1, i)
            return temp
        return helper(['a','e','i','o','u'], n, 'A')
'''
arr, n
for i in 
return helper(arr, )
'''