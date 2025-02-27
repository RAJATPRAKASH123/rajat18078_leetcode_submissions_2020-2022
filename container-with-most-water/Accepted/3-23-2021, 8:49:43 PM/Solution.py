// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0; right = n - 1 
        capacity = 0
        while left != right:
            capacity = max(capacity, (min(height[right], height[left]) * (right-left)))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1 
        return capacity