// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        arr.append(10000000000)
        n = len(arr)
        # Recursive function
        
        def helper(i, nextt):
            if i == -1:
                return 0
            if arr[i] < arr[nextt]:
                return max( helper(i-1, nextt), 1 + helper(i-1, i) )
            else:
                prev = -1
                for t in range(i, -1, -1):
                    if arr[t] < arr[nextt]:
                        prev = t
                        break
                if prev == -1:
                    return 0
                return max(1 + helper(t-1, t ), helper( t-1, nextt) )
            
        return helper(n-2, n-1) 