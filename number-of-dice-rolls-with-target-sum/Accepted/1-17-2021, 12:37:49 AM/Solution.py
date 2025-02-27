// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        dp = [[[-1 for i in range(d+3)] for j in range(f+3)] for k in range(target+3)] 
        
        def helper(d, f, target):
            temp = 0
            if target < 0 or d < 0:
                return 0
            
            if target == 0 and d == 0:
                return 1
            if d == 0:
                return 0
            if dp[target][f][d] != -1:
                return dp[target][f][d]
            
            for i in range(1,f+1):
                
                temp = (temp + helper(d-1, f, target-i))% (10**9 + 7)
            dp[target][f][d] = temp
            return temp
        
        return helper(d,f,target)

# class Solution:
#     def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
#         # dp = [[[-1 for i in range(d+3)] for j in range(f+3)] for k in range(target+3)] 
#         def helper(d, f, target):
#             if d == 0 and target == 0:
#                 return 1
#             if d <= 0 or target <= 0 or f <= 0:
#                 return 0
#             return helper(d-1, f, target - f) + helper(d, f-1, target)
            
            
        
#         return helper(d,f,target)

'''
for every (target, d) combination 
find previous f combinations for d-1 
and (target-1 to target-f) ka sum

d : dice
f : face
target

'''