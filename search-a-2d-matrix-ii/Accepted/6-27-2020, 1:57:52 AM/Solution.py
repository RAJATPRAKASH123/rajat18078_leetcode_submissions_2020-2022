// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, arr, key):
        if not arr:
            return False
        i = 0
        j = len(arr[0]) - 1
        while j >= 0 and i < len(arr):
            if arr[i][j] == key:
                return True
            if arr[i][j] < key:
                i += 1
            elif arr[i][j] > key:
                j -= 1
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        row_lptr = 0
        row_rptr = m-1
        col_lptr = 0
        col_rptr = n-1
        
        mr
        mc 
        arr[mr][mc] > key
        
        
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
        '''