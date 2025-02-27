// https://leetcode.com/problems/split-array-largest-sum

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if m == len(nums):
            return max(nums)
        low, high = max(nums), sum(nums)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        def checkIt(cur):
            nonlocal m
            last_pos = 0
            cur_subarrays = 0
            for i in range(1, len(nums)):
                if nums[i] - last_pos >= cur:
                    cur_subarrays += 1
                    last_pos = nums[i-1]
                if cur_subarrays == m:
                    return True
            
        res = float('-inf')
        while low <= high:
            cur = (low + high)//2
            # print(low, high)
            if checkIt(cur):
                low = cur + 1
                res = max(res, cur)
            else:
                high = cur - 1
        return res
        
'''
[7,2,5,10,8]  # sum = 32 -> 
2

cur = (10 + 32)//2 = 21

10 and 20 : (10+20)//2 = 15

 7  9  14  24  32
    
'''
    
    

    