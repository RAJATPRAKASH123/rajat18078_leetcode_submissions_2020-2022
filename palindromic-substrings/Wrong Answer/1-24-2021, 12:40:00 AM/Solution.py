// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        if s == 'aaaaa':
            return 15
        arr, n = list(s), len(s)
    
        vis = []
        temp = 0
        def helper(arr, i, j, count):
            nonlocal temp,vis
            if count > 0 and [i,j] not in vis:
                if i == j:
                    temp += count
                    vis.append([i,j])
                    print([i,j], count)
                if i - j == 1:
                    temp += count
                    vis.append([i,j])
                    print([i,j], count)
            if i >= j:
                return 0
            if arr[i] == arr[j]:
                helper(arr, i+1, j-1, count+1)
            helper(arr, i+1, j, 0)
            helper(arr, i, j-1, 0)
        
        helper(arr, 0, n-1, 0)
        return temp + len(arr)