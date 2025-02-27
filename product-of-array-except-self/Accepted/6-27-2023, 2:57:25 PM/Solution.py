// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod, right_prod = [1] * len(nums), [1] * len(nums)
        left_prod[0] = nums[0]
        for i in range(1, len(nums)):
            left_prod[i] = nums[i] * left_prod[i-1] 
        right_prod[len(nums)-1] = 1

        for i in range(len(nums)-2, -1, -1):
            right_prod[i] = nums[i+1] * right_prod[i+1] 
        # print(left_prod)
        # print(right_prod)
        return [right_prod[0]] + [left_prod[i] * right_prod[i+1] for i in range(0,len(nums)-1)]
'''
nums

return answer

answer[i] = product of all elements of nums except nums[i]


1 2 3 4
4 3 2 1

1  2  3 4
1  2  6 24 < left
24 12 4 1  < right ka


1 2  6  24
4 12 24 1


res = 24 12 8 6
1 1 

'''