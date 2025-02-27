// https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        index = -1
        for i in range(len(s)):
            if s[i]==" ":
                index = i
                continue
            break
        index += 1
        if index == len(s):
            return 0
        sign = 1
        if s[index] == '-' or s[index] == '+':
            if s[index] == '-':
                sign = 0
            index += 1
        res = 0
        while index < len(s) and '9' >= s[index] >= '0':
            res = res * 10 + ord(s[index]) - ord('0')
            index += 1
        if sign == 1:
            return min(res, 2**31 - 1)
        return max(res*-1, 2**(-31))