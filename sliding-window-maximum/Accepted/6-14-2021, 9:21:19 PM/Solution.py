// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = []
        res = []
        for i in range(len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            if i - queue[0] == k:
                queue.pop(0)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res
        
'''

Input: nums = [1,3,-1,-3,5,3,6,7]
k = 3

1, 3, -1

3 -> -1 ->

'''