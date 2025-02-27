// https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

#         def binary(num):
#             cur = ""
#             while num > 0:
#                 cur = str(num % 2) + cur
#                 num = num//2
                
#             return "0" * (32 - len(cur)) + cur
        # for i in range(len(nums)):
        #     nums[i] = binary(nums[i])
        res = 0
        # print(nums)
        for i in range(32):
            count = 0
            for j in range(len(nums)):
                if (nums[j] & (1 << i)) != 0:
                    count += 1
            if count % 3 != 0:
                res += 1 << i
        return res
            
            
'''
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        int n = nums.length;
        
        for(int i = 0; i < 32; i++) {
            int cnt = 0;
            for(int j = 0; j < n; j++) {
                if((nums[j]&(1<<i)) != 0) cnt++;
            }
            if((cnt%3) != 0) {
                ans|=(1<<i);
            }
        }
		return ans;
		}


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
