// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        return left + 1
                    
'''
distinct integers
1 2 3 5
4
'''
