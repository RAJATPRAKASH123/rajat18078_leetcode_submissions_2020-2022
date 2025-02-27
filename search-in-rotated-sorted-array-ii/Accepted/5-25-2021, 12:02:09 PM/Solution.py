// https://leetcode.com/problems/search-in-rotated-sorted-array-ii

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums[0] == nums[-1]:
            return target in nums
        def binSearch(nums, target):
            # find pivot
            left = 0; right = len(nums)-1
            while left < right:
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if left >= 0 and left <= len(nums) and nums[left] == target:
                return True
        
        def findPivot(nums):
            # find pivot
            left = 0; right = len(nums)
            while left < right:
                
                mid = (left + right)//2
                # print(left, right, mid)
                if nums[0] > nums[mid]:
                    right = mid
                else:
                    left = mid+1
            if left == len(nums):
                return -1
            return left
        k = findPivot(nums)
        # print(k)
        
        
        if k == -1 or k == len(nums):
            return binSearch(nums, target)
        elif target == nums[0]:
            return True
        elif target > nums[0]:
            return binSearch(nums[:k], target)
        else:
            return binSearch(nums[k:], target)