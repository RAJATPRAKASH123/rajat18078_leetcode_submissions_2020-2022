// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    # def mergesort
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        arr.sort(key = lambda a : a[1])
        
        bool_arr = [True]*len(arr)
        
        i = 0
        j = 1
        count = 0
        while  j < len(arr):
            if bool_arr[j] and arr[j][0] < arr[i][1]:
                bool_arr[j] = False
                count += 1
                i += 1
            else:
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
