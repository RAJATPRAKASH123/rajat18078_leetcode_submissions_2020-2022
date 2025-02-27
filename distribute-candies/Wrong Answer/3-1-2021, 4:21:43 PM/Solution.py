// https://leetcode.com/problems/distribute-candies

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eaten = set()
        ans = 0
        for candy in candyType:
            if candy not in eaten:
                ans += 1
                eaten.add(candy)
                if ans >= len(candyType):
                    return ans
        return ans