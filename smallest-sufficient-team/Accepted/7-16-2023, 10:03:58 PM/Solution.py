// https://leetcode.com/problems/smallest-sufficient-team

from collections import *
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        ans = [k for k in range(len(people))]
        tot = (1<< n)-1
        print(bin(tot))
        d = {}
        for i, skill in enumerate(req_skills):
            d[skill] = 1<<i
        mp = defaultdict(lambda : -1)
        def solve(i,vis):
            nonlocal n
            if vis == tot:
                return []
            if i == len(people):
                return [k for k in range(61)]
            if mp[(i,vis)] != -1:
                return mp[(i,vis)]
            ppl_skill = 0
            for skl in people[i]:
                ppl_skill |= d[skl]
            a = [i]+ solve(i+1, vis | ppl_skill)
            b = solve(i+1,vis)
            if len(a)<= len(b):
                mp[(i,vis)] = a
            else:
                mp[(i,vis)] = b
            return mp[(i,vis)]
        return solve(0,0)

            