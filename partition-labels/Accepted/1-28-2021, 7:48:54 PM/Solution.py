// https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        l = [-1 for i in range(26)]
        r = [-1 for i in range(26)]
        for i in range(len(s)):
            if l[ord(s[i])-97] == -1:
                l[ord(s[i])-97] = i
        for i in range(len(s)):
            r[ord(s[i])-97] = i
        
        print(l)
        print(r)
        cur, last = l[ord(s[0])-97], r[ord(s[0])-97]
        ans = []
        vis = set()
        for i in range(1,len(s)):
            if s[i] not in vis:
                vis.add(s[i])
                temp1, temp2 = l[ord(s[i])-97], r[ord(s[i])-97]
                # print(last-cur)
                if temp1 > last:
                    ans += [last-cur+1]
                    cur, last = temp1, temp2
                else:
                    last = max(last,temp2)
                    cur = min(temp1, cur)
        return ans + [len(s) - sum(ans)]
'''
abcdefg
'''