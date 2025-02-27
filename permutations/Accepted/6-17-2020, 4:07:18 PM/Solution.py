// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        k = len(nums)
        def helper(nums, tmp):
            nonlocal arr
            nonlocal k
            if len(tmp) == k:
                arr.append(tmp)
                return
            for i in range(len(nums)):
                helper(nums[:i] + nums[i+1:],tmp+[nums[i]])
        helper(nums,[])
        return arr