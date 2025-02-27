// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make

from collections import defaultdict
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        if coins[0] != 1:
            return 1
        count = defaultdict(int)
        for i in coins:
            count[i] += 1
        cur_min, cur_max = 1, 0
        coins = list(count.keys())
        for i in coins:
            if i == 1:
                cur_max = count[i]
                continue
            if i - cur_max > 1:
                break
            cur_max += i*count[i]
        return cur_max + 1
        
'''

coins : n length
ith : coins[i]


'''