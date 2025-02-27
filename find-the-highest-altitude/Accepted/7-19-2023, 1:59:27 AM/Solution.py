// https://leetcode.com/problems/find-the-highest-altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curAltitude = 0
        maxAltitude = curAltitude
        for g in gain:
            curAltitude += g
            maxAltitude = max(maxAltitude, curAltitude)
        return maxAltitude
'''
road trip

n + 1 points at different altitudes

0 with altitude equal to 0

gain of length n


'''