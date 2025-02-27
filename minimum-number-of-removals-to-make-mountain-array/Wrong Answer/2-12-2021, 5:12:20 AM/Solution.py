// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array

class Solution:
    def minimumMountainRemovals(self, arr: List[int]) -> int:
        
        n = len(arr)
        left_ith_lis = [0 for i in range(n)]
        right_ith_lis = [0 for i in range(n)]
        
        left_ith_lis[0] = 1
        for i in range(1, n):
            for prev in range(i):
                if arr[prev] < arr[i]:
                    left_ith_lis[i] = max(1 + left_ith_lis[prev], left_ith_lis[i])

            left_ith_lis[i] = max(left_ith_lis[i], 1)
        
        right_ith_lis[n-1] = 1
        for i in range(n-2,-1,-1):
            for nextt in range(i+1,n):
                if arr[nextt] < arr[i]:
                    right_ith_lis[i] = max(1 + right_ith_lis[nextt], right_ith_lis[i])

            right_ith_lis[i] = max(right_ith_lis[i], 1)
        ans = 0
        print(right_ith_lis, left_ith_lis)
        for i in range(n):
            ans = max(ans,right_ith_lis[i] + left_ith_lis[i] -1)
        return n - ans
        
'''
Approach : find maxm bitonic subsequence(maxm)
ans = len(arr) - maxm
'''