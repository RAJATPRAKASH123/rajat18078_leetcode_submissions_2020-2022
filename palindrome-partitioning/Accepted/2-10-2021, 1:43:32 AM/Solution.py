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
        
        def helper(i, ans=[]):
            nonlocal res
            if i == n:
                res.append(ans)
                return
            
            for k in range(i, n):
                # print(i, k)
                # if i == n:
                #     helper(k+1, ans + [i, i])
                if is_pal(i, k ):
                    helper(k+1, ans + [[i, k]] )
            return ans
        res = []
        papa = helper(0)
        fin_strings = []
        for i in res:
            temp = []
            for j in i:
                
                temp.append(s[j[0]:j[1]+1])
            fin_strings.append(temp)
        return fin_strings