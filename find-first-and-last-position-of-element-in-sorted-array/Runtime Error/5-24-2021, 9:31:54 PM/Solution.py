// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        def findFirst(target):
            left, right = 0, len(nums)

            while left < right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid
            return left
            
        
        first_occ = findFirst(target)
        if nums[first_occ] != target:
            return [-1,-1]
        else:
            last_occ = findFirst(target+1)
            
            return [first_occ,last_occ-1]