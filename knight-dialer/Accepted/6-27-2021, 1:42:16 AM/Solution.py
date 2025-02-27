// https://leetcode.com/problems/knight-dialer

class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[[-1 for i in range(n+1)] for j in range(3)] for i in range(4)]
        phone_pad = [[1, 1, 1],[1, 1, 1], [1, 1, 1], [0, 1, 0]]
        def dfs(arr, i, j, steps):
            if dp[i][j][steps] != -1:
                return dp[i][j][steps]
            if steps == 0:
                return 1
            moves = [(-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (2, 1)]
            res = 0
            for x, y in moves:
                pos_x, pos_y = i + x, j + y
                if 0 <= pos_x < 4 and 0 <= pos_y < 3 and arr[pos_x][pos_y] == 1:
                    res += dfs(arr, pos_x, pos_y, steps - 1)
            dp[i][j][steps] = res 
            return res
        numbers = 0
        for i in range(4):
            for j in range(3):
                if i == 3 and j == 0:
                    continue
                if i == 3 and j == 2:
                    continue
                numbers += dfs(phone_pad, i, j, n-1) % (10**9 + 7) 
        return numbers % (10**9 + 7)