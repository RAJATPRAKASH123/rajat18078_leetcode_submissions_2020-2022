// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution:
    def numberOfSteps (self, num: int) -> int:
        return bin(num).count("1") * 2 + bin(num).count("0")-2