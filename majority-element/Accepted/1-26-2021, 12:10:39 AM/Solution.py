// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        candidate = arr[0]
        count = 1
        for i in arr[1:]:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -=1
        return candidate