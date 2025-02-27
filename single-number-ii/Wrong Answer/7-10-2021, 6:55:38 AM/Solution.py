// https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        def binary(num):
            cur = ""
            while num > 0:
                cur += str(num % 2)
                num = num//2
            return "0" * (32 - len(cur)) + cur
        for i in range(len(nums)):
            nums[i] = binary(nums[i])
        res = 0
        for i in range(32):
            count = 0
            for j in range(len(nums)):
                if nums[j][i] == '1':
                    count += 1
            if count % 3 != 0:
                res += 2 ** (32 - i-1)
        return res
            
            
'''
3 3 3 5

    11
    11
    11
   101

'''
