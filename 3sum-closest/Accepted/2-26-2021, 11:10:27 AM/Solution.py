// https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        res = float('inf')
        
        for i in range(n):
            cur_target = target - nums[i]
            left, right = 0, n-1
            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue
                lhs = nums[left] + nums[right]
                if lhs > cur_target:
                    right -= 1
                else:
                    left += 1
                if abs(lhs + nums[i] - target) < abs(res - target):
                    res = lhs + nums[i]
        return res
                

# -4 -1 1 2