// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jump = float('inf') 
        if len(nums) == 1:
            return 0
        def min_jumps(i=0, count=0):
            nonlocal min_jump
            if i >= len(nums)-1:
                min_jump = min(count, min_jump)
                return
            if nums[i] == 0:
                return
            #recursive calls
            for next in range(i+1, min(len(nums), nums[i]+i+1)):
                min_jumps(next, count+1)
        min_jumps()
        return min_jump