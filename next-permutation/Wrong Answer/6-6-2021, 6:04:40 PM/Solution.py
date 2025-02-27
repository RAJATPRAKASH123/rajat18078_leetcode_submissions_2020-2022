// https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, 0, -1):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    # flag = True
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[j+1:] = sorted(nums[j+1:])
                    return
        nums.sort()