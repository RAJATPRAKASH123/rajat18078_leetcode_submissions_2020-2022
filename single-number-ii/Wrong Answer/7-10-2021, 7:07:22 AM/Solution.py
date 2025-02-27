// https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        def binary(num):
            cur = ""
            while num > 0:
                cur = str(num % 2) + cur
                num = num//2
                
            return "0" * (32 - len(cur)) + cur
        for i in range(len(nums)):
            nums[i] = binary(nums[i])
        res = 0
        print(nums)
        for i in range(32):
            count = 0
            for j in range(len(nums)):
                if nums[j][i] == '1':
                    count += 1
            if count % 3 != 0:
                # print(i, count)
                res += 2 ** (32 - i-1)
        return res
            
            
'''
2 0
1 1
    16



3 3 3 5

['00000000000000000000011001010111',
 '00000000000000000000000001011111', 
 '00000000000000000000000000010011', 
 '00000000000000000000011001010111', 
 '00000000000000000000000000010011', 
 '00000000000000000000011001010111', 
 '00000000000000000000000000010011']
25 4
27 7
28 1
29 4
30 7
31 7



'''
