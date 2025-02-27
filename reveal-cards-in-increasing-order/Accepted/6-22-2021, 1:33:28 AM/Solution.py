// https://leetcode.com/problems/reveal-cards-in-increasing-order

from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        deck = deque(deck)
        res = deque([deck.popleft()])
        turn = 0
        while deck:
            if turn == 0:
                res.appendleft(res.pop())
            else:
                res.appendleft(deck.popleft())
            turn ^= 1
        return list(res)