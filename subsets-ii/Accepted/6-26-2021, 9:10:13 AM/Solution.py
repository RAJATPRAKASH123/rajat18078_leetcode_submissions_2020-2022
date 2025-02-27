// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        def helper(start = 0, cur = []):
            subsets.append(cur[:])
            if start == len(nums):
                return 
            for next in range(start, len(nums)):
                
                if next != start and nums[next] == nums[next-1]:
                    continue
                cur.append(nums[next])
                helper(next+1, cur)
                cur.pop()
        helper()
        return subsets