// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        
        left, right = 0, len(arr) # range where we can find our target
        while left < right: # or left <= right or ...
            mid = left + (right-left)//2
            
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
            
        return left