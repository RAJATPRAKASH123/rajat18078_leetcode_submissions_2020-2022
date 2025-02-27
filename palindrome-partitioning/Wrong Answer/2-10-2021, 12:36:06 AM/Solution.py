// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def is_pal(i, j):
            if i == j:
                return True
            temp = s[i:j+1]
            if  temp == temp[::-1]:
                return True
            
            return False
        def helper(i):
            if i == n:
                return []
            ans = []
            for k in range(i, n):
                if is_pal(i, k ):
                    ans += [[i, k]] + helper(k+1)
            return ans
        papa = helper(0)
        res = []
        temp = []
        for i in papa:
            if i[1] != n-1:
                temp += [s[i[0]:i[1]+1]]
            else:
                res.append(temp + [s[i[0]:i[1]+1]])
                temp = []
        return res