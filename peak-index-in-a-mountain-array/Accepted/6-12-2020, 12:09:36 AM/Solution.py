// https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1,len(A)):
            if A[i] < A[i-1]:
                return i-1