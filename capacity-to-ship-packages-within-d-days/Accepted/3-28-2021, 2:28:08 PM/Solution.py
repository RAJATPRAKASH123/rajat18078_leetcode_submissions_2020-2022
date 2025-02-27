// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights: List[int], d: int) -> int:
        low = max(weights)
        for i  in range(1, len(weights)):
            weights[i] += weights[i-1]
        
        high = weights[-1]
        res = -1
        
        def checkAt(cur):
            nonlocal d
            cur_days = 1; last_pos = 0
            for i in range(len(weights)):
                if weights[i] - last_pos > cur:
                    cur_days += 1
                    last_pos = weights[i-1]
                if cur_days > d:
                    return False
            return True
                
        while low <= high:
            cur = (low + high)//2
            if low == high and res == -1:
                res = low
                break
            if checkAt(cur):
                high = cur - 1
                res = cur
            else:
                low = cur + 1
        return res
        
        
'''
D days
ith : weights[i]


'''