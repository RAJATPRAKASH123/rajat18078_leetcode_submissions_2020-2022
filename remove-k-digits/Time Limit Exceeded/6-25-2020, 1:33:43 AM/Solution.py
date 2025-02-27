// https://leetcode.com/problems/remove-k-digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        l = len(num)
        i = 1
        arr = num
        if len(arr) == 1 and k == 1:
            return "0"
        while i < len(arr) and k > 0:
            if arr[i] >= arr[i-1]:
                i += 1
                if k > 0 and i == len(arr):
                    i = 0
                continue
            del arr[i-1]
            k -= 1
            if i > 1:
                i -= 1
                continue
            else:
                i += 1

        ans = ""
        for i in arr:
            ans += i
        return str(int(ans))