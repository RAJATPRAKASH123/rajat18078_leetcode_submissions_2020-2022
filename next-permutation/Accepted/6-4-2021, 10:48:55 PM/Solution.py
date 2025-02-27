// https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums)-1, 0, -1):
            print(i)
            if nums[i-1] < nums[i]:
                index = i-1
                break
        if index == -1:
            nums.reverse()
            return 
        print(index)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                nums[index+1:] = nums[index+1:][::-1]
                return 