// https://leetcode.com/problems/reduce-array-size-to-the-half

from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        count = defaultdict(int)
        for i in arr:
            count[i] += 1
        ans = []
        for i in count.values():
            ans.append(i)
        ans.sort()
        ans.reverse()
        temp = 0
        for i in range(len(ans)):
            temp += ans[i]
            if temp >= len(arr)//2:
                return i+1
        
