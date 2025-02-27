// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left = 0
        cur_res = k
        # traversal of right index
        for right in range(n):
            if arr[right] == 1:
                cur_res = max(cur_res, right - left + 1)
                continue
            else:
                k -= 1
            if k < 0:
                # maintaining left index
                while left < n and arr[left] != 0:
                    left += 1
                if left == n:
                    break
                left += 1
                k += 1
            cur_res = max(cur_res, right - left + 1)
        return cur_res
'''
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]

'''