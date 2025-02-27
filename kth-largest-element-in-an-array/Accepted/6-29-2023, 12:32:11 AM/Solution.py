// https://leetcode.com/problems/kth-largest-element-in-an-array

from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in nums:
            heappush(q, i)
            if len(q) > k:
                heappop(q)
        return heappop(q)