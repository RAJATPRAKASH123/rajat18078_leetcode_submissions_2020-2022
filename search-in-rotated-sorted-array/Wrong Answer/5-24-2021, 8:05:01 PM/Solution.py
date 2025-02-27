// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        #first index whose value is less than nums[0]
        def binSearch_mod(nums):
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left+right)//2
                if nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    right = mid
            if nums[left] > nums[0]:
                left = -1
            return left
        k = binSearch_mod(nums)
        
        def binSearch(arr, target):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left+right)//2
                # print(left, right, mid)
                if arr[mid] == target:
                    return mid
                if arr[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        
        if k == -1:
            return binSearch(nums,target)
        elif nums[0] <= target:
            return binSearch(nums[:k], target)
        else:
            res = binSearch(nums[k:], target)
            if res == -1:
                return -1
            return k + res