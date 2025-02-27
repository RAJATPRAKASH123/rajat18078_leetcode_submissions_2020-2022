// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr = []
        tup = ['(', ')']
        for i in s:
            if not arr:
                arr.append(i)
                continue
            if arr[-1] == i:
                arr.append(i)
                continue
            if i == tup[1] and arr[-1] == tup[0]:
                arr.pop()
            else:
                arr.append(i)
        return len(arr)