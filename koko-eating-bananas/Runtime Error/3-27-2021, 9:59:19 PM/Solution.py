// https://leetcode.com/problems/koko-eating-bananas

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        low, high = 0, piles[-1]
        res = -1
        
        def checkAt(cur):
            nonlocal h
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/cur)
            if hours <= h:
                return True
        
        while low <= high:
            cur = (low + high)//2
            # print(low, high, cur)
            if checkAt(cur):
                high = cur - 1
                res = cur
            else:
                low = cur + 1
        return res
        
'''
n piles of bananas

ith : piles[i]
guards come back in h hours

k : bananas per hour eating speed


'''