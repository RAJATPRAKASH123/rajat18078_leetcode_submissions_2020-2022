// https://leetcode.com/problems/kth-largest-element-in-an-array

from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p_q = []
        for i in nums:
            heappush(p_q, i)
            if len(p_q) > k:
                heappop(p_q)
        return heappop(p_q)