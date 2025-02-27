// https://leetcode.com/problems/stone-game-ii

class Solution:
    def stoneGameII(self, arr: List[int]) -> int:
        
        def helper(arr, i, m, turn):
            
            if i == len(arr):
                return 0
            temp = 0
            if turn:
                temp2 = float('-inf')
                for x in range(1, 2*m + 1):
                    r = min(len(arr), i+x)
                    # print(temp2, x)
                    temp2 = max(temp2, sum(arr[i:r]) + helper(arr, r, max(x, m), not turn))
                    # print(temp2, x)
                temp += temp2
                print(temp)
            else:
                temp2 = float('inf')
                for x in range(1, 2*m + 1):
                    r = min(len(arr), i+x)
                    # print(temp2, x)
                    temp2 = min(temp2, -sum(arr[i:r]) + helper(arr, r, max(x, m), not turn))
                    # print(temp2, x)
                temp += temp2
                print(temp)
            return temp
            
        dif = (sum(arr) + helper(arr, 0, 1, True))//2
        return dif