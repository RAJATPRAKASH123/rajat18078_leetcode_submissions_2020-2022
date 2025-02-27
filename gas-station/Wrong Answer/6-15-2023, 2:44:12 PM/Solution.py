// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        newArr = [i - j for i, j in zip(gas, cost)]
        maxIndex = 0
        for i in range(len(newArr)):
            if newArr[i] > newArr[maxIndex]:
                maxIndex = i
        totalGas = 0
        drivePossible = True
        for i in newArr[maxIndex:] + newArr[0:maxIndex]:
            totalGas += i
            if totalGas < 0:
                drivePossible = False
        return maxIndex if drivePossible else -1
'''
n gas stations -> 
a circular route 
ith: amount of gas -> gas[i]
unlimited gas tank - cost[i]

unique soln. guaranteed


question? Longest consecutive sub-circular array i.e. Sum( gas[i, j]) for each i, j > Sum( cost[i, j]) for each i, j

Let's create a new array with difference gas - cost

alt. quest?
newArr -> longest consecutive subarray with max sum

[1,2,3,4,5], cost = [3,4,5,1,2]
-2, -2, -2, 3, 3
'''