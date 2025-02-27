// https://leetcode.com/problems/largest-sum-of-averages

from collections import defaultdict
class Solution:
    def largestSumOfAverages(self, arr: List[int], k: int) -> float:
        if k == 1:
            return sum(arr)/len(arr)
        preSum = [0]*(len(arr) + 1)
        for i in range(1, len(arr) + 1):
            preSum[i] = preSum[i-1] + arr[i-1]
        memo = defaultdict(int)
        def helper(prev=0, cur=1, count=0):
            nonlocal k
            temp = (prev, cur, count)
            if temp in memo:
                return memo[temp]
            if cur == len(arr):
                if count == k - 1:
                    return (preSum[cur] - preSum[prev])/(cur-prev)
                else:
                    return float('-inf')
            if count == k:
                return float('-inf')
            memo[temp] = max((preSum[cur] - preSum[prev])/(cur-prev) + helper(cur,cur+1, count + 1), helper(prev, cur+1, count))
            return memo[temp]
        return helper()