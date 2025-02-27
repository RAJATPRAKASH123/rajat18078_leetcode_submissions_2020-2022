// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = deque([])
        for i in range(1, 1001):
            for j in range(1, 10001):
                val = customfunction.f(i, j)
                if val > z:
                    break
                if val == z:
                    res.append([i, j])
        return res