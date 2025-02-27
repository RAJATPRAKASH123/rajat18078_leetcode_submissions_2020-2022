// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array

class Solution:
    def getSumAbsoluteDifferences(self, arr: List[int]) -> List[int]:
        n = len(arr)
        pre_sum = [0]* (n + 1)
        
        for i in range(n):
            pre_sum[i+1]= pre_sum[i]+arr[i]
        ans = [0]*n
        
        for i in range(n):
            ans[i] = (pre_sum[n]-pre_sum[i]) - (arr[i]*(n-i)) + abs((pre_sum[i]-pre_sum[0]) - (arr[i]*(i)))
        return ans