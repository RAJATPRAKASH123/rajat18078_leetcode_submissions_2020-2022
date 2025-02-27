// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        arr = [0 for i in range(len(nums)+1)]
        for i in nums:
            arr[i] += 1
        f, s = -1, -1
        for i in range(1, len(nums)+1):
            if arr[i] == 2:
                f = i
            if arr[i] == 0:
                s = i
        return [f,s]
            
'''

'''