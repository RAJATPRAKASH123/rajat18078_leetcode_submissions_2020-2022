// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_length = len(word)
        if word_length > m*n:
            return False
        def dfs( letter_posn, i, j ):
            if letter_posn == word_length:
                return True
            if letter_posn == word_length -1 and not visited[i][j] and board[i][j] == word[letter_posn] :
                return True
            
            if board[i][j] == word[letter_posn] and not visited[i][j]:
                visited[i][j] = True
                l,r,u,d = False, False, False, False
                if j < n-1:
                    u = dfs(letter_posn+1, i, j+1)
                if j > 0:
                    d = dfs(letter_posn+1, i, j-1)
                if i < m - 1:
                    r = dfs(letter_posn+1, i+1, j)
                if i > 0:
                    l = dfs(letter_posn+1, i-1, j)
                ans = u or d or r or l
                if not ans:
                    visited[i][j] = False
                return ans
        
        for i in range(m):
            for j in range(n):
                visited = [[False for j in range(n)] for i in range(m)]
                if dfs(0, i, j):
                    return True
        return False
            
            

'''
m, n board
a word
[["a","b","b","a","b"],
["a","a","b","b","a"],
["a","a","a","a","b"],
["a","a","a","b","a"],
["a","a","a","a","a"],
["a","b","a","b","b"],
["a","b","b","a","b"]]
"abbbbaababaa"
'''