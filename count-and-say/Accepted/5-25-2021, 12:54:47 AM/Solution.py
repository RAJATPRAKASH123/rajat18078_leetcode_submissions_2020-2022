// https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int) -> str:
        arr = ["1", "11"]
        for j in range(3, n+1):
            count = 1
            res = ""
            for i in range(1, len(arr[-1])):
                if arr[-1][i] == arr[-1][i-1]:
                    count += 1
                else:
                    res += str(count) + arr[-1][i-1]
                    count = 1
                if i == len(arr[-1])-1:
                    res += str(count) + arr[-1][i]
            arr.append(res)
        return arr[n-1] # n=5; "111221"