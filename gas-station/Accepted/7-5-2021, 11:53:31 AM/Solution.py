// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        possible = 0
        for g, c in zip(gas, cost):
            possible += g - c
        if possible < 0:
            return -1
        start = 0
        reach = 0
        for i in range(len(gas)):
            reach += gas[i] - cost[i]
            if reach < 0:
                reach = 0
                start = i + 1
        return start