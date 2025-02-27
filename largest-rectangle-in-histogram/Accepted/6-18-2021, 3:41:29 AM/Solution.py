// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nextSmaller = [0]*n
        prevSmaller = [0]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prevSmaller[i] = stack[-1]
            else:
                prevSmaller[i] = -1
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nextSmaller[i] = stack[-1]
            else:
                nextSmaller[i] = n
            stack.append(i)
        res = 0
        cur = 0
        # print(nextSmaller, prevSmaller)
        for right, left in zip(nextSmaller, prevSmaller):
            res = max((right-left-1) * heights[cur], res)
            cur += 1
        return res