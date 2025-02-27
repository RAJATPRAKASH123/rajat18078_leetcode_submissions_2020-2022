// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        left = 0
        right = len(arr)-1
        while left < right:
            if arr[left] + arr[right] == target:
                break
            if arr[left] + arr[right] > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]
            
'''

a + b = 0

-7 -2 2 13

'''