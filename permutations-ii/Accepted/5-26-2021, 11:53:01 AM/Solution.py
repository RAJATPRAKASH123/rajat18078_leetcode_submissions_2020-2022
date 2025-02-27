// https://leetcode.com/problems/permutations-ii

from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def all_perms( visited = set(), cur_res = []):
            # print(cur_res, visited)
            if len(visited) == len(nums):
                res.add(tuple([int( i) for i in cur_res] ))
                return
            for i in range(len(nums)):
                if str(i) not in visited:
                    temp = visited.copy()
                    temp.add(str(i))
                    all_perms(temp, cur_res.copy() + [str(nums[i])] )
        all_perms()
        return list(res)