// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        visited = 0
        while i < len(nums):
            temp = i + nums[i]
            if temp >= len(nums)-1:
                return True
            if temp > visited:
                visited = temp
            if nums[i] == 0 and visited <= i:
                return False
            i += 1