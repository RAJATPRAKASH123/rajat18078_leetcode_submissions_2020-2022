// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        word_length = len(word)
        
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
                return u or d or r or l
            # visited[i][j] = False # This is the back-tracking LMAOOOOO
        
        for i in range(m):
            for j in range(n):
                visited = [[False for j in range(n)] for i in range(m)]
                if dfs(0, i, j):
                    return True
                print(visited)
                break
            break
        return False
            
            

'''
m, n board
a word
[[True, True, True, True], 
[False, False, True, True], 
[False, False, True, True]]
'''