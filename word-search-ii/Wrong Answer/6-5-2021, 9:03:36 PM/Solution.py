// https://leetcode.com/problems/word-search-ii

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        
        def exist(word, i, j, cur=0):
            if cur == len(word):
                return True
            
            if len(board) > i >= 0 and len(board[0]) > j >= 0 and word[cur] == board[i][j]:
                temp = board[i][j] 
                board[i][j] = "*"
                a = exist(word, i+1, j, cur+1)
                b = exist(word, i-1, j, cur+1)
                c = exist(word, i, j+1, cur+1)
                d = exist(word, i, j-1, cur+1)
                board[i][j] = temp
                return a or b or c or d
            return False
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if exist(word, i, j):
                        res.append(word)
        return res