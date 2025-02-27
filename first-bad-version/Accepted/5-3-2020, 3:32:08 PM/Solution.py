// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper( f, n):
            if n - f <= 1:
                if isBadVersion(f):
                    return f
                else:
                    return n
            if isBadVersion((f+n)//2):
                return helper(f, (f+n)//2)
            else:
                return helper((f+n)//2, n)
        return helper(1,n)
        