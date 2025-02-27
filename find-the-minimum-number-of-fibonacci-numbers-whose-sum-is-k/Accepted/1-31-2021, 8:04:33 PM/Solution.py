// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        arr = [1,1]
        while arr[-1] < k:
            arr.append(arr[-1]+arr[-2])
        if arr[-1] == k or arr[-2] == k:
            return 1
        i = -1
        ans = 0
        while k != 0:
            if arr[i] > k:
                i -= 1
                continue
            ans += (k//arr[i])
            k -= (k//arr[i]) * arr[i]
            i -= 1
        return ans
'''
1
1
2
3
5
8
13
21
34
55
'''