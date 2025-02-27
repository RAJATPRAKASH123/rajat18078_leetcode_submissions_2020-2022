// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        l,r = set(), set()
        for i in range(len(edges)):
            l.add(edges[i][0])
            r.add(edges[i][1])
        ans = []
        for i in l:
            if i not in r:
                ans += [i]
        return ans