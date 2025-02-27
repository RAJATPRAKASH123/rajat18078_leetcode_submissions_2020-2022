// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeated = -1
        cur_sum = 0
        real_sum = n*(n+1)/2
        for i in nums:
            
            if nums[abs(i)-1] < 0:
                repeated = abs(i)
            nums[abs(i)-1] *= -1
            cur_sum += abs(i)
            
        return [repeated, int(real_sum - cur_sum + repeated)]
    
    
'''
n*(n+1)/2

'''