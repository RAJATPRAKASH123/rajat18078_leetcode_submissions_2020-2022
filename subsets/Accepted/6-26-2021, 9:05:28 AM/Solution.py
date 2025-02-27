// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i=0, cur = []):
            res.append(cur[:])
            if i == len(nums):
                return
            for next in range(i, len(nums)):
                cur.append(nums[next])
                helper(next+1, cur)
                cur.pop()

        helper()
        return res