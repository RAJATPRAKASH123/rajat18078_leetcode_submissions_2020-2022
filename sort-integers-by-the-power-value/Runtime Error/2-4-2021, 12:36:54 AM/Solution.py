// https://leetcode.com/problems/sort-integers-by-the-power-value

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        dp=[-1 for i in range(4000)]
        
        def helper(i):
            if i == 1:
                return 0
            if dp[i] != -1:
                return dp[i]
            if i%2 == 0:
                dp[i] = 1 + helper(i//2)
                return dp[i]
            dp[i] = 1 + helper(3*i + 1)
            return dp[i]   
        arr = [i for i in range(lo, hi+1)]
        for i in range( hi-lo+1):
            arr[i] = [arr[i], helper(arr[i])]
        arr.sort(key = lambda x : x[1])
        print(arr)
        return arr[k-1][0]
'''
1
2-1
3-10-5-16-8-4-2-1
4-2-1
5-16-8-4-2-1
6-3
'''