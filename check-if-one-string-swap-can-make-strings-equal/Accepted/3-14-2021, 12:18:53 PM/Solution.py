// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        arr1 = []; arr2 = []
        for i, j in zip(s1, s2):
            if i != j:
                arr1.append(i)
                arr2.append(j)
                count += 1
        if count > 2:
            return False
        if set(arr1) == set(arr2):
            return True
        return False