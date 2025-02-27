// https://leetcode.com/problems/stone-game

from collections import defaultdict
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # "Alice" : 0
        memo = defaultdict(int)
        def gameHelperOptimal(turn = 0, left_index = 0, right_index = len(piles) - 1):
            alice_profit = 0 #  stones of alice - stones of bob
            if (turn, left_index, right_index) in memo:
                return memo[(turn, left_index, right_index)]
            if left_index > right_index:
                return 0
            if turn == 0:
                # Alice will choose
                # 1. choose left
                left_chosen_profit = piles[left_index] + gameHelperOptimal(turn ^ 1, left_index + 1, right_index)
                # 2. choose right
                right_chosen_profit = piles[right_index] + gameHelperOptimal(turn ^ 1, left_index, right_index - 1)
                alice_profit = max(left_chosen_profit, right_chosen_profit)
            else:
                # Bob will choose
                # 1. choose left
                left_chosen_profit =  -piles[left_index] + gameHelperOptimal(turn ^ 1, left_index + 1, right_index)
                # 2. choose right  
                right_chosen_profit = -piles[right_index] + gameHelperOptimal(turn ^ 1, left_index, right_index - 1)
                alice_profit = min(left_chosen_profit, right_chosen_profit)
            
            memo[(turn, left_index, right_index)] = alice_profit
            return memo[(turn, left_index, right_index)]
        if gameHelperOptimal() > 0:
            return True
            
'''

4 2 9 3 5 3

A: 4
B: 3
2 9 3 5
A: 5
B: 3
A : 9
B : 2

A = 4 + 5 + 9
B : 3 + 5 + 2
'''