// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                res = max(res, i - left + 1)
                continue
            k -= 1
            if k < 0:
                while nums[left] != 0:
                    left += 1
                left += 1
            res = max(res, i - left + 1)
        return res
'''
sliding window
left, right
take count of 1s
traverse right

'''