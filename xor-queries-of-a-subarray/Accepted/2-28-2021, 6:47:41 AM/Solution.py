// https://leetcode.com/problems/xor-queries-of-a-subarray

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pre_xor = [0 for i in range(len(arr)+1)]
        pre_xor[0] = arr[0]
        
        for i in range(1, len(arr) ):
            pre_xor[i] = pre_xor[i-1] ^ arr[i]
            
        ans = [0 for i in range(len(queries))]
        idx = 0
        for left, right in queries:
            if left == 0:
                ans[idx] = pre_xor[right]
            else:
                ans[idx] = pre_xor[right] ^ pre_xor[left-1]
            idx += 1
        return ans