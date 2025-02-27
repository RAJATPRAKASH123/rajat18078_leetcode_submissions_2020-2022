// https://leetcode.com/problems/wiggle-subsequence

from collections import defaultdict
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        def wiggle(i, prev=-1, wants=None):
            res = 0
            if i == len(nums):
                return 0
            if (i, prev, wants) in dp:
                return dp[(i, prev, wants)]
            if wants is None:
                res = max( 1 + wiggle(i+1, i, 1), 1 + wiggle(i+1, i, -1))
            else:
                if wants == 1 and nums[prev] < nums[i]:
                    res = max( 1 + wiggle(i+1, i, -1), wiggle(i+1, prev, 1))
                elif wants == -1 and nums[prev] > nums[i]:
                    res = max( 1 + wiggle(i+1, i, 1), wiggle(i+1, prev, -1))
                else:
                    res = wiggle(i+1, prev, wants)
            dp[(i, prev, wants)] = res
            return res
        
        ans = wiggle(0)
        # print(dp)
        return ans