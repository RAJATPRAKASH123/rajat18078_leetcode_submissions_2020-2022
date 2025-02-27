// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        rev = 0
        real_x = x
        while x > 0:
            last = x%10
            rev += last * 10**(int(log10(x)))
            x = x//10
        return rev == real_x
    
'''
12343

3*log10(x)

'''