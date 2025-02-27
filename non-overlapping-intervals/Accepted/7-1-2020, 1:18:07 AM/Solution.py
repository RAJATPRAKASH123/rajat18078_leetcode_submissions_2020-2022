// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    # def mergesort
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        arr.sort(key = lambda a : a[1])
        print(arr)
        i = 0
        j = 1
        count = 0
        while  j < len(arr):
            if arr[j][0] < arr[i][1]:
                count += 1
                j += 1
            else:
                i = j
                j += 1
                    
        return count
    
    
'''
        1    7  9    15
            6    10
    
    
        1 7
        6 10
        4 10
        9 15
'''
