// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        arr=[0]*(n+1)
        arr[1],arr[2] = 1,1
        for i in range(3,n+1):
            arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
        return arr[n]