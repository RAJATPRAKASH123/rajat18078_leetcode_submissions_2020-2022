// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to

from collections import defaultdict
class Solution:
    def groupThePeople(self, arr: List[int]) -> List[List[int]]:
        
        
        d = defaultdict(list)
        temp = 0
        for i in range(len(arr)):
            if arr[i] in d.keys():
                d[arr[i]].append(i)
            else:
                d[arr[i]] = [i]
        ans = []
        for i in d.keys():
            for j in range(0,len(d[i]), i):
                ans += [d[i][j:j+i]]
        return ans