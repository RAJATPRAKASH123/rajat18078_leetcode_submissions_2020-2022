// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        while x > 9:
            left_digit = x // ( 10 ** (int(log10(x)) ))
            right_digit = x % 10
            
            if right_digit != left_digit:
                return False
            x = x//10 #removing least significant digit
            x = x % ( 10 ** (int(log10(x)) )) #removing most significant digit
        return True
        
        
'''
Follow up: Could you solve it without converting the integer to a string?
'''