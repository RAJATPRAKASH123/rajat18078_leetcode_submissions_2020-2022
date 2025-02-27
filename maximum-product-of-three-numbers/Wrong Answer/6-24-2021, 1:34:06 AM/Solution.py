// https://leetcode.com/problems/maximum-product-of-three-numbers

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        last, sec_last = float('inf'), float('inf')
        first, sec, third = float('-inf'), float('-inf'), float('-inf')
        for i in nums:
            if i >= first:
                third = sec
                second = first
                first = i
            elif i >= second:
                third = second
                second = i
            elif i >= third:
                third = i
            else:
                pass
            if i <= last:
                sec_last = last
                last = i
                continue
            elif i <= sec_last:
                sec_last = i
            else:
                pass
        return max(last*sec_last*first, first, sec, third)