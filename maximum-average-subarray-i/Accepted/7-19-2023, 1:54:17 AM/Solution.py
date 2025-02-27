// https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])/k
        maxSum = cur
        for i in range(len(nums)-k):
            cur -= nums[i]/k
            cur += nums[i+k]/k
            maxSum = max(cur, maxSum)
        return maxSum
'''
nums
n elements 

k 

contiguos subarray i.e. length == k


'''