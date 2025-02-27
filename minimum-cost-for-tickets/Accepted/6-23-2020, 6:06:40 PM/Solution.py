// https://leetcode.com/problems/minimum-cost-for-tickets

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        arr = [0]*365
        for i in days:
            arr[i-1] = 1
        for i in range(0,365):
            if arr[i] == 0:
                if i != 0:
                    arr[i] = arr[i-1]
                continue
            f, s, t = 0, 0, 0
            if i > 0:
                f = arr[i-1]
            if i >= 7:
                s = arr[i-7]
            if i >= 30:
                t = arr[i-30]
            arr[i] = min(f + costs[0], s + costs[1], t + costs[2])
        return arr[364]