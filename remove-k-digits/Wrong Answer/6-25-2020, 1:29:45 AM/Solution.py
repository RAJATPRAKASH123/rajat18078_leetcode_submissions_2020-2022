// https://leetcode.com/problems/remove-k-digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        l = len(num)
        i = 1
        arr = num
        while i < len(arr) and k > 0:
            if arr[i] >= arr[i-1]:
                i += 1
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