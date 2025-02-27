// https://leetcode.com/problems/magnetic-force-between-two-balls

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        res = 0        
        low, high = 0, position[-1]
        def checkIt(cur):
            nonlocal m
            cur_balls = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= cur:
                    cur_balls += 1
                    last_pos = position[i]
                if cur_balls == m:
                    return True
        while low <= high:
            cur = (low + high)//2
            if checkIt(cur):
                low = cur + 1
                res = max(res, cur)
            else:
                high = cur - 1
        return res