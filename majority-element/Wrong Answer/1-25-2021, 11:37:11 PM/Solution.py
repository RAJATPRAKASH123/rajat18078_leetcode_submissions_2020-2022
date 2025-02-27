// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        current = arr[0]
        count = 1
        temp_count = 0
        for i in range(1,len(arr)):
            if arr[i] == current:
                count += 1
            else:
                temp_count += 1
                if temp_count > count:
                    current = arr[i]
                    count = temp_count-count
        return current
'''

2 2   1 1 1   2 2
-> 
2, count : 1
2, count : 2
1, count 
'''