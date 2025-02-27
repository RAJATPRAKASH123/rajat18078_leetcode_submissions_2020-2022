// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        temp = 0
        # dp = [[[-1 for i in range(d+3)] for j in range(f+3)] for k in range(target+3)] 
        def helper(d, f, target):
            nonlocal temp
            if target < 0 or d < 0:
                return 0
            
            if target == 0 and d == 0:
                return 1
            if d == 0:
                return 0
            
            for i in range(1,f+1):
                # print(temp,f)
                temp += helper(d-1, f, target-i)
            return temp
        
        return helper(d,f,target)

'''


d : dice
f : face
target

'''