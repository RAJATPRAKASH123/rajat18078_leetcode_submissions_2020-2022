// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        minm = float('inf')
        res = 0
        for i in range(len(nums)):
            res = max(nums[i] - minm, res)
            minm = min(minm, nums[i])
        return res

'''
prices : for each day
[7,1,5,3,6,4]
 7 1 1 1 1 1
 6 6 6 6 6 4
 
profit : maximize

program -> 1 sec - 10 sec

1 sec -> python 10**7 ~ 10**8 operations
C++/C -> 10**8 operations
JAV -> 1/5 * 10**8 operations

7 1
1
-> 4
6

ith per hain -> yeh kabhi na kabhi toh solution ka part banega
left , right
'''

