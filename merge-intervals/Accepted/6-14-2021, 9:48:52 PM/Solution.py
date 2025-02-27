// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])
        
        left, right = intervals[0][0],  intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            begin, end = intervals[i][0],  intervals[i][1]
            if begin > right:
                res.append([left, right])
                left, right = begin, end
                continue
            right = max(right, end)
            
        res.append([left, right])
        return res