// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
            
        count = 0 # keeps track of when left == right 
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                for k in range(j, len(arr)):
                    
                    left, right = 0, 0
                    if i == 0:
                        left = arr[j-1]
                    else:
                        left = arr[j-1] ^ arr[i-1]
                    right = arr[k] ^ arr[j-1]
                    if left == right:
                        count += 1
        return count