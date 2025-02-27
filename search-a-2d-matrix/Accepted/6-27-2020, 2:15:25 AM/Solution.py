// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, arr: List[List[int]], key: int) -> bool: 
        if not arr:
            return False
        i, j = 0, len(arr) - 1
        while i < j:
            print(i,j)
            m = (i + j)//2
            if arr[m][len(arr[0])-1] == key:
                return True
            if arr[m][len(arr[0])-1] < key:
                i = m + 1
            else:
                j = m 
        row_bin_search = i
        if len(arr) == 1:
            row_bin_search = 0
        i, j = 0, len(arr[0]) - 1
        print(row_bin_search)
        while i <= j:
            m = (i + j)//2
            if arr[row_bin_search][m] == key:
                return True
            if arr[row_bin_search][m] > key:
                j = m - 1
            else:
                i = m + 1
        return False
        
        '''
  [1,   3,  5,  7],<- i
  [10, 11, 16, 20],
  [23, 30, 34, 50]  
  
                   <- j     
        
        
        '''