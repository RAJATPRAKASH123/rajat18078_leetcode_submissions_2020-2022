// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVeisB

class Solution:
    def firstBadVersion(self, n):
        for i in range(1,n+1):
            if isBadVersion(i):
                return i
        """
        :type n: int
        :rtype: int
        """
        