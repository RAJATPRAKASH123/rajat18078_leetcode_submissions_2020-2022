// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        if (n//10 == 0):
            if (n == 1 or n == 7):
                return True
            return False
        temp = 0
        for i in str(n):
            temp += int(i)**2
        return self.isHappy( temp)