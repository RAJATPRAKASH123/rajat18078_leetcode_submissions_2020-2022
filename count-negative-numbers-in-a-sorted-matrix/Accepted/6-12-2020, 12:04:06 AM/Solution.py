// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def leftPositive(arr, l , r):
            if arr[0] >= 0:
                return 0
            if arr[len(arr)-1] < 0:
                return len(arr)
            m = (l + r)//2
            if arr[m] >= 0 and m != 0 and arr[m-1] < 0:
                return m
            if arr[m] < 0:
                return leftPositive(arr, m+1, r)
            return leftPositive(arr, l, m)
        count = 0
        for i in grid:
            count += leftPositive(i[::-1], 0, len(i)-1)
        return count