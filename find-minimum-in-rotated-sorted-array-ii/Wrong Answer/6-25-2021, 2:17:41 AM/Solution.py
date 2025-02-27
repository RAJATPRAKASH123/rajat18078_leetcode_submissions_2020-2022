// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 1
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[0] if left == len(nums) else nums[left]