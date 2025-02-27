// https://leetcode.com/problems/maximum-product-of-three-numbers

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        cur = nums[-1] * nums[-2] * nums[-3]
        if nums[0] >= 0 or nums[1] >= 0:
            return cur
        return max(cur, nums[0] * nums[1] * nums[-1])