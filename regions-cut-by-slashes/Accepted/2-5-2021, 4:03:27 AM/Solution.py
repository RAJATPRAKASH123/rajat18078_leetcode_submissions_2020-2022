// https://leetcode.com/problems/regions-cut-by-slashes

class Solution:
    def regionsBySlashes(self,arr: List[str]):
        for i in range(len(arr)):
            arr[i] = list(arr[i])
            
        new_arr = [[0 for i in range(3*len(arr))] for j in range(3*len(arr))]

        for i in range(len(arr)):
            for j in range (len(arr[i])):
                if arr[i][j] == '/':
                    new_arr[3*i+2][3*j] = 1
                    new_arr[3*i][3*j+2] = 1
                    new_arr[3*i+1][3*j+1] = 1
                    
                if arr[i][j] == "\\":
                    new_arr[3*i+2][3*j+2] = 1
                    new_arr[3*i][3*j] = 1
                    new_arr[3*i+1][3*j+1] = 1
        
        def helper(arr, i, j):
            if i == -1 or j == -1 or i == len(arr) or j == len(arr):
                return 
            if arr[i][j] == 0:
                arr[i][j] = 1
                helper(arr, i, j+1)
                helper(arr, i+1, j)
                helper(arr, i-1, j)
                helper(arr, i, j-1)
            
            
        count = 0
        for i in range(len(new_arr)):
            for j in range(len(new_arr)):
                if new_arr[i][j] == 0:
                    count += 1
                    helper(new_arr, i, j)
        return count
'''
[[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 1, 0],
[0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0]]

'''
        
            