// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        
        left, right = 0, len(arr)-1 # range where we can find our target
        while left < right: # or left <= right or ...
            mid = left + (right-left)//2
            
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
            
        return left if arr[left] == target else left+1