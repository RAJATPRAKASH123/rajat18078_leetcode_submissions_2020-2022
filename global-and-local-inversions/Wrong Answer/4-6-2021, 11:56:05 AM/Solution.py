// https://leetcode.com/problems/global-and-local-inversions

class Solution:
    def isIdealPermutation(self, arr: List[int]) -> bool:
        res_global = 0
        # global inversions
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    res_gloabal+= 1
        res_local = 0
        # local inversions
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                res_local += 1
        return res_local == res_global