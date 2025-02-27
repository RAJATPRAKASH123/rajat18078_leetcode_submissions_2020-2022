// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            if i < n-1 and nums[i] == nums[i+1]:
                continue
            cur = -nums[i]
            left, right = 0, n-1
            while left < right:
                if left == i :
                    left += 1
                    continue
                if right == i :
                    right -= 1
                    continue
                lhs = nums[left] + nums[right]
                if lhs == cur:
                    ans = sorted([nums[left], nums[right], nums[i]])
                    res.add(tuple(ans))
                if lhs > cur:
                    right -= 1
                else:
                    left += 1


        return list(res)
                
'''
a + b = -c 
lhs   = rhs
'''