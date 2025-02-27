// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVeisB

class Solution:
    def firstBadVersion(self,n):
        def helper(l,r):
            if isBadVersion(1):
                return 1
            i = (l+r)//2
            if not isBadVersion(i-1) and isBadVersion(i) :
                return i
            if isBadVersion(i):
                return helper(l,i)
            return helper(i+1,r)
        return helper(1,n)
        """
        :type n: int
        :rtype: int
        """
        