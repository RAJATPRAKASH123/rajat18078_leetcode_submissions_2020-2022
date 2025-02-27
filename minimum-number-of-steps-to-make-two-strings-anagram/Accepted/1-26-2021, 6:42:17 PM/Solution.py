// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        arr1 = [0]*26
        arr2 = [0]*26
        for i in s:
            arr1[ord(i)-97] += 1
        for i in t:
            arr2[ord(i)-97] += 1
        extras = [0]*26
        for i in range(26):
            extras[i] = arr2[i] - arr1[i]
        count = 0
        return sum([abs(i) for i in extras])//2
            
'''
bab
aba

leetcode

c, 1
d, 1
e, 3
l, 1
o, 1
t, 1
[1, 1, -1, -2, 1, 1, -1, 1, 1, 0]
practice
a, 1
c, 2
e, 1
i, 1
p, 1
r, 1
t, 1


'''