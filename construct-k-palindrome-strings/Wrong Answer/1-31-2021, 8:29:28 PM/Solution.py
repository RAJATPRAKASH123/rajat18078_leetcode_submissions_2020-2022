// https://leetcode.com/problems/construct-k-palindrome-strings

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        count = [0]*26
        for i in s:
            count[ord(i)-97] += 1
        temp = 0
        for i in count:
            temp += i%2
        if temp > k:
            return False
        return True
        
'''
    
'''