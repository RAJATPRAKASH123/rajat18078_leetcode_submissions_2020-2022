// https://leetcode.com/problems/uncrossed-lines

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[-1 for i in range(len(nums2))] for j in range(len(nums1))]
        def helper(i,j):
            if i == len(nums1):
                return 0
            if j == len(nums2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if nums1[i] == nums2[j]:
                return 1 + helper(i+1, j+1)
            dp[i][j] = max(helper(i,j+1), helper(i+1, j))
            return dp[i][j]
        return helper(0,0)