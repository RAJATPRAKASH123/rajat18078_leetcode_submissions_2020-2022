// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = max(candies)
        ans=[False]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= temp:
                ans[i] = True
        return ans