// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        rev = 0
        temp = x
        while x > 0:
            rev += x // (10**int(log10(x)))
            x = x % (10**int(log10(x)))
            if x == 0:
                break
            rev *= 10
        # print(rev, temp)
        return rev == temp
'''


'''